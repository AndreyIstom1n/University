from math import sqrt, ceil
from random import randint

def modulate(n, m):
    return n - n // m * m

def joinArray(a, s=', '):
    return s.join(map(str, a))

def components(n, k=2):
    b, m = 0, n
    while m % k == 0:
        b += 1
        m //= k
    return b, m #кол-во делений и остаток

def extendedEuclideanAlgorithm(n, m):
    if n == 0:
        return m, 0, 1
    d, x, y = extendedEuclideanAlgorithm(m % n, n)
    return d, y - m // n * x, x   #НОд n&m, коэфы x&y, d=n*x+m*y

def fastPowerMod(a, k, n):
    p = 1
    while k > 0:
        if k % 2 == 1:
            p = modulate(p * a, n)
        a = modulate(a * a, n)
        k //= 2
    return p

def isPotentialPrime(p, k=5):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if p < 2 or p in primes:
        return True
    for i in primes:
        if p % i == 0:
            return False
        if i * i > p:
            return True
    pa, pb = p // 10, p - 1
    b, m = components(pb)
    for i in range(1, k + 1):
        l, f, a = 1, False, randint(pa, pb)
        for _ in range(b + 1):
            q = fastPowerMod(a, m * l, p)
            l *= 2
            if q == 1 or q == p - 1:
                f = True
                break
        if not f:
            return False
    return True

def RabenMillerPrime(p):
    p += 1 + p % 2
    f = isPotentialPrime(p)
    while not f:
        p += 2
        f = isPotentialPrime(p)
    return p
#обратное число к n по modp
def inverseMod(n, p):
    n = modulate(n, p)
    g = extendedEuclideanAlgorithm(n, p)
    return g[1] % p if g[0] == 1 else 0

#disk log x по основанию g для a modp
def babystepGiantstep(p, g, a):
    m = ceil(sqrt(p))
    b = fastPowerMod(g, m, p)
    u, v = [b], [modulate(g * a, p)]
    for _ in range(m):
        w = modulate(b * u[-1], p)
        if w == u[0]:
            break
        u.append(w)

    for _ in range(m):
        if v[-1] in u:
            break
        v.append(modulate(g * v[-1], p))

    i = 1 + u.index(v[-1])
    j = len(v)
    return modulate(m * i - j, p - 1)

def factorBase(t):
    S = [2]
    for _ in range(t - 1):
        S.append(RabenMillerPrime(S[-1]))
    return S

def factorization(g, S):
    f = []
    for i in S:
        if g % i == 0:
            b, g = components(g, i)
            f.append(b)
        else:
            f.append(0)
    return -1 if g > 1 else f

def FBFactorization(p, g, x, tc, S, fe=0):
    A, b = [], []
    gk = x if fe == 0 else modulate(x * fastPowerMod(g, fe, p), p)
    for k in range(1, p):
        f = factorization(gk, S)
        gk = modulate(g * gk, p)
        if f == -1:
            continue
        A.append(f)
        b.append(k)
        if len(A) == tc:
            break
    return A, b  #матр коэф и в-ор свободных чл

def GausSolverMod(A, b, p):
    li, lj = len(A[0]), len(A)
    A = [j + [b[i]] for i, j in enumerate(A)]
    for i in range(li):
        nn0 = 0
        A[i:] = sorted(A[i:], key=lambda x: x[i], reverse=True)
        if A[i][i] == 0:
            break

        while nn0 < lj - i:
            if A[i + nn0][i] == 0:
                b = A[i:i + nn0]
                b.reverse()
                A[i:i + nn0] = b
                break
            nn0 += 1

        nsh = 0
        for j in range(i, i + nn0):
            if extendedEuclideanAlgorithm(p, A[j][i])[0] == 1:
                break
            nsh += 1
        else:
            break

        if nsh != 0:
            shift = A[i:i + nsh]
            A[i][i:i + nn0 - nsh] = A[i + nsh:i + nn0]
            A[i + nn0 - nsh:i + nn0] = shift

        ia = inverseMod(A[i][i], p)
        A[i][i:] = [1] + [0 if j == 0 else modulate(j * ia, p) for j in A[i][i + 1:]]
        for j in range(lj):
            if i == j or A[j][i] == 0:
                continue
            A[j][i:] = [0] + [modulate(m - A[j][i] * A[i][i + l + 1], p) for l, m in enumerate(A[j][i + 1:])]

    return [i[-1] for i in A[:li]]

def orderCount(p, g, a, c=10, t=5):
    S = factorBase(t)
    A, b = FBFactorization(p, g, g, t + c, S)
    x = GausSolverMod(A, b, p - 1)
    A, b = FBFactorization(p, g, a, 1, S, 1)
    return modulate(sum([x[i] * A[0][i] for i in range(t)]) - b[0], p - 1)

def start(n, g, a):
    names = ['шаг младенца шаг великана', 'исчисления порядка']
    xbsgs = babystepGiantstep(n, g, a)
    xoc = orderCount(n, g, a, 1, 4)
    return (f'Дискретный логарифм от {a} по основанию {g} по модулю {n} равен:\n' +
            f'Методом {names[0]}: {xbsgs}\n' +
            f'Методом {names[1]}: {xoc}\n' +
            f'равенство: {xbsgs == xoc and a == fastPowerMod(g, xoc, n)}\n')

# Ввод данных n-модуль (простой) 307, g-основание меньше n 23, a-результат 0<=a<n-1 97
try:
    n, g, a = map(int, input("Введите n, g и a через пробел: ").split())
    print(start(n, g, a))
except ValueError:
    print("Ошибка: Пожалуйста, введите три целых числа.")

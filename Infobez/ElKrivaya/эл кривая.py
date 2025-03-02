from math import sqrt
from random import randint
def modulate(n, m):
    return n - n // m * m
def codes (s, alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
    return [1 + alf.index(i) for i in s]
def components(n, k = 2):
    b, m = 0, n
    while m % k == 0:
        b += 1
        m //= k
    return b, m
def extendedEuclideanAlgorithm(n, m):
    if n == 0:
        return m, 0, 1
    d, x, y = extendedEuclideanAlgorithm(m % n, n)
    return d, y - m // n * x, x
def fastPowerMod(a, k, n):
    p = 1
    while k > 0:
        if k % 2 == 1:
            p = modulate(p * a, n)

        a = modulate(a * a, n)
        k //= 2

    return p
def isPotentialPrime(p, k = 5):
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
def sqrtMod(x, p):
    x = modulate(x, p)
    for i in range(p):
        if modulate(i * i, p) == x:
            return i
    return -1
def ellipticY(x, p, a, b):
    return sqrtMod(b + x * (a + x * x), p)
def onCurve(x, y, p, a, b):
    if x is None:
        return True
    y0 = ellipticY(x, p, a, b)
    return y == y0 or y == p - y0
def firstEllipticPoint(p, a, b, x = -1):
    y = -1
    while x < p:
        if y != -1:
            break
        x += 1
        y = ellipticY(x, p, a, b)
    else:
        return -1, -1
    return x, y
def inverseMod(n, p):
    n = modulate(n, p)
    g = extendedEuclideanAlgorithm(n, p)
    return g[1] % p if g[0] == 1 else 0
def ellipticSum(p, a, x, y, z, w):
    if x is None:
        return z, w
    elif z is None:
        return x, y
    elif x != z:
        l = (w - y) * inverseMod(z - x, p)
    elif y == w and y != 0:
        l = (3 * x * x + a) * inverseMod(2 * y, p)
    else:
        return None, 0
    l = modulate(l, p)
    z = modulate(l * l - x - z, p)
    return z, modulate(l * (x - z) - y, p)
def ellipticCurveOrder(p, a, b):
    x, r = -1, 0
    while x < p:
        x = firstEllipticPoint(p, a, b, x)[0]
        if x == -1:
            break
        r += 2
    return r
def EllipticCurveCypher(p, a = 1, b = 0, k = 151, xStart = -1, x0 = -1, y0 = -1):
    if x0 == -1:
        x0, y0 = firstEllipticPoint(p, a, b, xStart)
    x, y, xd, yd = None, 0, x0, y0
    for i in bin(k)[2:][::-1]:
        if i == '1':
            x, y = ellipticSum(p, a, x, y, xd, yd)
        xd, yd = ellipticSum(p, a, xd, yd, xd, yd)
    return x0, y0, x, y, onCurve(x0, y0, p, a, b), onCurve(x, y, p, a, b)
def ellipticPointOrder(p, a, b, x, y, n):
    if isPotentialPrime(n):
        return 1 if x is None else n
    j, z, w = 0, None, 0
    for i in range(2, n):
        if n % i == 0:
            z, w = ellipticSum(p, a, z, w, *EllipticCurveCypher(p, a, b, i - j, x0 = x, y0 = y)[2:4])
            if z is None:
                return i
            j = i
    return n
def start(s):
    a, b = 1, 0
    c = codes(s)
    prod = int(''.join(map(str, c)))
    p = RabenMillerPrime(prod)
    sqp = 2 * sqrt(p)
    ans = EllipticCurveCypher(p, a, b, xStart = 0)
    co = ellipticCurveOrder(p, a, b)
    po = ellipticPointOrder(p, a, b, *ans[:2], co)
    return ('Коды инициалов: {}\n'.format(c) +
            'p = {} > {}\n\n'.format(p, prod) +
            ('P = ({0}, {1})\n151 P = ' + ('E' if ans[2] is None else '({2}, {3})') + '\n\nДействительно ли они принадлежат эллиптической кривой: {4}, {5}\n\n').format(*ans) +
            'Порядок кривой: {0}\nВерна ли теорема Хассе: {1}\n{2:.3f} ≤ {0} ≤ {3:.3f}\n\n'.format(co, abs(p + 1 - co) <= sqp, p + 1 - sqp, p + 1 + sqp) +
            'Порядок точки P: {0}\n{0} P = ({1}, {2})'.format(po, *EllipticCurveCypher(p, a, b, po)[2:4]))
s = input("Введите строку: ")
result = start(s)
print("Результат:", result)

from decimal import Decimal, ROUND_UP, getcontext
from random import randint
from time import time
#n%m
def modu(n, m):
    return n - n // m * m
def mult(a):
    p = 1
    for i in a:
        for _ in range(i[1]):
            p *= i[0]
    return p
def format(s, a):
    for i in a:
        s += '\n{}^{}'.format(*i)
    return s
#разлагает n на степень k
def co(n, k=2):
    b, m = 0, n
    while m % k == 0:
        b += 1
        m //= k
    return b, m  #кол-во делений, остаток

def fPM(a, k, n):
    p = 1
    while k > 0:
        if k % 2 == 1:
            p = modu(p * a, n)
        a = modu(a * a, n)
        k //= 2
    return p
def Prime(p, k=5):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if p < 2 or p in primes:
        return True
    for i in primes:
        if p % i == 0:
            return False

    pa, pb = p // 10, p - 1
    b, m = co(pb)
    for i in range(1, k + 1):
        l, f, a = 1, False, randint(pa, pb)
        for _ in range(b + 1):
            q = fPM(a, m * l, p)
            l *= 2
            if q == 1 or q == p - 1:
                f = True
                break
        if not f:
            return False
    return True
#делители
def f2factor(n):
    if n in [1, 3, 5]:
        return 1, n
    x = n.sqrt().quantize(Decimal('1.'), rounding=ROUND_UP)
    r = x * x - n
    while True:
        y = r.sqrt()
        if y % 1 == 0:
            return int(x - y), int(x + y)
        r += 2 * x + 1
        x += 1
def fFactors(n):
    i, a = -1, list(f2factor(n))
    while i < len(a) - 1:
        i += 1
        if not Prime(a[i]):
            for j in f2factor(Decimal(a[i])):
                a.append(j)
            a.pop(i)
            i -= 1
    return sorted([[i, a.count(i)] for i in set(a)])
def fastFactorization(n):
    ans = 'Разложение:'
    if n % 2 == 0:
        b, n = co(n)
        ans = format(ans, [[2, b]])
    f = fFactors(n)
    return format(ans, f) + '\n\nРазложение верно: {}'.format(n == mult(f))
input_value = input("Введите число для разложения: ")
n = Decimal(input_value)
getcontext().prec = len(str(n))
t1 = time()
s = fastFactorization(n)
t2 = time()
print(s)
print('Затраченное время: {:.6f} с'.format(t2 - t1))
#183483903543663118800683335500060438797379801801396319200491

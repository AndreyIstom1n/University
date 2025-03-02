import random


def checkprimenum(p, a):
    for i in a:
        if (p % i == 0):
            return False
        return True


#ak^i modn =p
def stepmodul(i, p, ak, n):
    while i > 0:
        s = i % 2
        if s == 1:
            p = (p * ak) % n
        ak = (ak * ak) % n
        i = (i - s) // 2
    return p


def test(numtest, p, bit, m, b):
    answ = False
    print("Номер теста: ", numtest)
    print("p= ", p)
    f = random.randint(1, bit - 1)
    a = random.getrandbits(f)
    print("a= ", a)
    g = stepmodul(m, 1, a, p)
    print("g= ", g)
    for j in range(0, b + 1):
        if (g == 1) or (g == (p - 1)) and j == 0:
            answ = True
            print("j= ", j, " g= ", g)
            break
        if (g < (p - 1)) and 0 < j < b:
            g = pow(g, 2) % p
        print("j= ", j, " g= ", g)
        if (g == 1) or (g == (p - 1)) and j == 0:
            answ = True
            break
        if (g == 1) and j > 0:
            break
        if g == p - 1 and 0 < j < b:
            answ = True
        if j <= b and g == p - 1:
            answ = True
    return answ


bit = int(input("Количество бит: "))
p = random.getrandbits(bit)
p = bin(p)[2:]
while len(p) != bit:
    p += "1"
if p[-1] != "1":
    p = p[:-1]
    p = p + "1"
print("bin p= ", p)
p = int(p, 2)
print("p= ", p)
a = [2, 3, 5, 7, 11, 13, 17, 19, 23]
answ = False

flag=0
while answ is False:
    while checkprimenum(p, a) is False:
        p += 2
    b, s = 0, p - 1
    while s % 2 == 0:
        b += 1
        s //= 2
    print("b= ", b)
    m = int((p - 1) // pow(2, b))
    count = 0
    for i in range(1, 6):
        answ = test(i, p, bit, m, b)
        
        if answ is False and flag<1:
            print("Тест провален. p изменено")
            flag+=1
            break
        else:
            print("Тест ", i, " завершен успешно")
            count += 1
            prob = (0.25) ** count
            print("Вероятность того, что число простое после теста ", i, ": ", 1 - prob)
    if count == 5:
        print("Тесты завершены, p может быть простым")
        print("Вероятность того, что p - простое: ", 1 - ((0.25) ** count))
        answ = True
    else:
        p += 2
        

import math
import random
#a^d mod(n) метод быстрого возведения в степень
def MyPow(d,a,n):
    i = d
    p = 1
    ak = a
    while (i > 0):
        s = i % 2
        if (s == 1):
            p = (p * ak) % n

        ak = (ak * ak) % n
        i = (i - s) / 2
    S = p
    return S

def IsSimpleTogether(p, arr):
    for i in arr:
        if (p % i == 0):
            print("Число делится на ", i)
            return False
    return True

def BecomingPrime(p,arr):
    while(not IsSimpleTogether(p, arr)):
        print("p = ",p," делится на небольшие простые числа. Добавляем к нему 2")
        p+=2
    return p
def IsSimple(a):
    k = 0
    for i in range(1, a):
        if (a % i == 0):
            k += 1
    if k > 1:
        return False
    else:
        return True



def Test(z,p,b):
    flag=True
    if (z == 1) or (z == (p - 1)):
        return True
    j=1

    b=b

    while j < b:
        print("При j = ",j," z =",z , " p =",p)
        if (z == 1) and j > 0:
            return False
        if (z < (p - 1)) and j < b:
            z = MyPow(2, z, p)

        j += 1
        if (z == (p - 1)):
            return True

    if j == b and (z != (p - 1)):
         return False
    return True

#p-1=(2^b)*m (m -нечетное)
def FindB(p):
    b=0
    p =p-1
    while p % 2 == 0:
        b += 1
        p //= 2
    return b


def SimpleNum():
    print('\nГенерация простых чисел\n\n')
    k_test=5

    k = int(input("Введите количество бит числа:"))
    p = random.getrandbits(k)

    binar = bin(p)[2:]
    print("Получившиееся число с ", k, " бит p = ", p)
    print("Получившийся бинарный вид цисла выше = ", binar)
    if(len(binar)<k):
        binar=binar.ljust(k,"1")
        print("Бинарный вид был дополнен символом 1 и получилось = ", binar)
    if binar[-1] != "1":
        binar = binar[:-1]
        binar = binar + "1"
        print("Вид при изменении младшего бита для нечетности = ", binar)
    p = int(binar, 2)
    print("Получившийся p  = ", p)
    p_start=p

    list_simple=list()
    for i in range(3,256,2):
        if(IsSimple(i)):
            list_simple.append(i)
    print("Массив простых чисел до 256: \n",list_simple)

    print("Число тестов = ", k_test)




    count=0
    while True:
        p=BecomingPrime(p,list_simple)
        print("Получаем новое p= ",p," \nОно не делится на небольшие простые числа.")
        b=FindB(p)
        print("Число целочисленных делений числа p на 2 будет b = ",b)
        m = (p - 1) // pow(2, b)
        print("Число m = ", m)
        count_s_test = 0


        print("----- Процесс проверки -----")
        for i in range(0, k_test):
            rs = random.randint(1, k - 1)
            a = random.getrandbits(rs)
            bi = bin(a)[2:]
            if (len(bi) < rs):
                bi = bi.ljust(rs, "1")
            a = int(bi, 2)
            a+=1
            print("Случайно получившиеся число бит до k будет ", rs)


            print("Случайно получившиеся число, которое является меньше p будет ", a)
            z=MyPow(m,a,p)
            print("z из основы =", z)


            if Test(z,p,b):
                print("Проверка номер ", i+1, " из ", k_test, " была пройдена.")
                count_s_test +=1
                count += 1
            else:
                print("!!!Проверка номер ", i+1, " из ", k_test, " не была пройдена.!!!")
                break


        if(count_s_test<5):
            print("Проверка не была пройдена. Добавляем 2 к p \n\n")
            p+=2
        else:

            print("Проверка была пройдена. Число ниже является простым\n", p, "\nИзначально p было \n", p_start," \n2 было добавлено к изначальному числу ",(p-p_start)/2,
                  " раз\nПростое число было успешно найдено")
            print("Вероятность, что будет составное ",pow(1/4, count))
            return p
            break
        #break

    answ=""

def DiffHelm():

    p=SimpleNum()
    print('\nПротокол Диффи-Хеллмана\n\n')
    print("p =", p)
    k = p - 1 #простые делители
    print("k =", k)

    delit=[]
    for i in range (2,k):
        if k%i==0 and IsSimple(i):
            delit.append(i)

    fi = k #для примитивных корней
    for i in range(0,len(delit)):
        fi *= (1 - 1 / delit[i])
    fi = int(fi)
    print("Число примтивных чисел = ", fi)

    print("Простые делители числа к : ", delit)

    primitiv=[]
    counter=0

    for j in range(1, k):
        for i in range(len(delit)):
            if (int(MyPow(delit[i],j , p)) == 1):
                break
            if (i == len(delit)-1):
                primitiv.append(j)
                counter += 1
        if counter==fi:
            break


    g = random.choice(primitiv)
   # if len(primitiv)==fi:
    #    print("Число примитивных совпадает с числом фи")
    #else:
    #    print("Число примитивных не совпадает с числом фи")
    print("Выбранное примитивное значение:", g)
    xa = random.randint(1, p - 1)
    xb = random.randint(1, p - 1)

    ya = MyPow(xa, g, p)

    yb = MyPow(xb, g, p)

    print("Закрытый ключ Alice Xa =", xa,"\nОткрытый ключ Alice Ya =", ya,"\nЗакрытый ключ Bob Xb =", xb,"\nОткрытый ключ Bob Yb =", yb)

    if (MyPow(xa, yb, p) == MyPow(xb, ya, p)):
        print("Успешно сформирован секретный ключ")
    secret_key = MyPow(xb * xa, g, p)
    secret_key_a = MyPow(xa, yb, p)
    secret_key_b = MyPow(xb, ya, p)
    if(secret_key==secret_key_a and secret_key_b==secret_key):
        print("Секретные ключи для Alice и Bob совпадают друг с другом и с общим секретным ключом")
    else:
        print("Секретные ключи для Alice и Bob не совпадают друг с другом и с общим секретным ключом")

    print("Секретный ключ = ", secret_key)

DiffHelm()

def simple(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return 0
    return 1


def delen(n):
    i = 2
    a = []
    while i * i <= n:
        while n % i == 0:
            a.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        a.append(n)
    return a


#остаток, e, k
def NOD(x1, y1):
    if x1 == 0:
        return y1, 0, 1
    else:
        div, x, y = NOD(y1 % x1, x1)
    return div, y - (y1 // x1) * x, x


def coding(list_symb, e, n):
    list_cod = list()
    for j in list_symb:
        i = e  #счетчик с e
        p = 1  #ответ
        ak = j  #основ
        while i > 0:
            s = i % 2  #остаток по модулю
            if s == 1:
                p = (p * ak) % n
            ak = (ak * ak) % n
            i = (i - s) / 2
        list_cod.append(p)
    return list_cod


def decoding(list_cod, d, n):
    list_decod = list()
    for j in list_cod:
        i = d
        p = 1
        ak = j
        while i > 0:
            s = i % 2
            if s == 1:
                p = (p * ak) % n
            ak = (ak * ak) % n
            i = (i - s) / 2
        list_decod.append(p)
    return list_decod


def num_to_alp(list_num, alp):
    res = ""
    for i in list_num:
        index = int(i) - 1
        if 0 <= index < len(alp):
            res += alp[index]
    return res


def fhash(list_symb1, new_txt, H0, alp):
    i = 0  #пор.номер символа
    for j in new_txt:
        list_symb1.append(alp.find(j) + 1)
        H0 = ((pow(H0 + list_symb1[i], 2)) % n)
        i += 1
    return H0


def eds(d, r, n):
    p = 1
    i = d
    ak = r
    while (i > 0):
        s = i % 2
        if s == 1:
            p = (p * ak) % n
        ak = (ak * ak) % n
        i = (i - s) / 2
    return p


print("1. Ключи")
p = int(input("Введите простое число p из первой сотни: "))
q = int(input("Введите простое число q из первой сотни: "))
flag = 0

while flag != 1:
    if simple(p) == 0 or p > 99:
        print("Неверное значение p. Повторите попытку")
        p = int(input())
    else:
        flag = 1
flag1 = 0
while flag1 != 1:
    if simple(q) == 0 or q > 99:
        print("Неверное значение q. Повторите попытку")
        q = int(input())
    else:
        flag1 = 1

n = p * q
print("n= ", n)
fi_n = (p - 1) * (q - 1)
print("fi_n= ", fi_n)
a = delen(fi_n)
b = set(a)
a = list(b)

d = int
flag = 0
for i in range(q + 1, fi_n):
    flag = 0
    b = simple(i)
    for j in a:
        if i % j != 0:
            flag += 1
    if flag == len(a) and b == 1:
        d = i
        if d == 23:
            break
print("d= ", d)
e = NOD(d, fi_n)[1]
k = NOD(d, fi_n)[2]
print(NOD(d,fi_n))
print("e= ", e)
print("k= ", k)
print("e= ", e, "mod", fi_n)
while (e < 0):
    e += fi_n
print("Тогда e= ", e)
print("Открытый ключ: (", e, ", ", n, ")")
print("Закрытый ключ: (", d, ", ", n, ")")

print("2. Зашифрование")
alp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
txt = str(input("Введите ФИО:"))[:3]
txt = txt.upper()
print("Полученный текст: ", txt)
while len(txt) < 3:
    print("Непавильно введённые данные. Повторите попытку")
    txt = str(input("Введите ФИО:"))[:3]
    print("Полученный текст:  ", txt)

list_symb = list()  #номер символа
list_cod = list()  #зашифрованный текст
list_decod = list()  #расшифрованный текст

for i in txt:
    list_symb.append(alp.find(i) + 1)
list_cod = coding(list_symb, e, n)

print("Зашифрованный текст: ", list_cod)
list_decod = decoding(list_cod, d, n)

print("3. Расшифрование")
new_txt = num_to_alp(list_decod, alp)
print("Расшифрованный текст: ", list_decod, " -> ", new_txt)

print("4. Функция хэширования")
H0 = int(input("Введите H0: "))
new_txt = input("Введите текст: ")
new_txt = new_txt.upper()
list_symb1 = list()
r = fhash(list_symb1, new_txt, H0, alp)
print("r= ", r)
print("5. Электронная цифровая подпись")
print("S= ", eds(d, r, n))
print("Проверка")
print("H= ", eds(e, eds(d, r, n), n))
if r == eds(e, eds(d, r, n), n):
    print("Успешно")
else:
    print("Ошибка")
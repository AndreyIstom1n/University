#текст в бинарную запись
def binary(text: str, encoding='cp1251') -> str:
    return ' '.join(
        bin(i)[2:].rjust(8, '0') for i in text.encode(encoding)
    )


#сумма двоичных
def sum_binary_strings(X, R0):
    summa = ""
    per = 0
    reverse_x = X[::-1]
    reverse_r = R0[::-1]
    for i in range(len(reverse_x)):
        if reverse_x[i] != " ":
            if int(reverse_x[i]) + int(reverse_r[i]) + per == 2:
                summa += "0"
                per = 1
            elif int(reverse_x[i]) + int(reverse_r[i]) + per == 3:
                summa += "1"
                per = 1
            else:
                summa += str(int(reverse_x[i]) + int(reverse_r[i]) + per)
                per = 0
        else:
            summa += " "
    return summa[::-1]


#из двоичного в десятичное
def binary_to_decimal(number):
    decimal, i = 0, 0
    while number != 0:
        dec = number % 10
        decimal = decimal + dec * pow(2, i)
        number = number // 10
        i += 1
    return decimal


#поиск по таблице
def search_table(table, list_num2, list_num1):
    list_num3 = []
    list_bin2 = []
    for i in range(len(list_num1)):
        value = table[list_num2[i]][i]  #переменная значения из таблицы
        list_num3.append(value)
        list_bin2.append(str((format(value, 'b'))).rjust(4, "0"))
    return list_num3, list_bin2


#сдвиг
def shift_string(pred_f: str, shift: int) -> str:
    f = ""
    for i in range(len(pred_f)):
        f += pred_f[(i + shift) % len(pred_f)]
        if (len(f) + 1) % 9 == 0:
            f += " "
    return f


#вычисление по модулю 2
def calculate_module2(f: str, L0: str) -> str:
    R1 = ""
    for i in range(len(f)):
        if f[i] != " ":
            R1 += str((int(f[i]) + int(L0[i])) % 2)
        else:
            R1 += " "
    return R1


print("Шифр: ГОСТ 28147-89")
table = (
    (1, 13, 4, 6, 7, 5, 14, 4),
    (15, 11, 11, 12, 13, 8, 11, 10),
    (13, 4, 10, 7, 10, 1, 4, 9),
    (0, 1, 0, 1, 1, 13, 12, 2),
    (5, 3, 7, 5, 0, 10, 6, 13),
    (7, 15, 2, 15, 8, 3, 13, 8),
    (10, 5, 1, 13, 9, 4, 15, 0),
    (4, 9, 13, 8, 15, 2, 10, 14),
    (9, 0, 3, 4, 14, 14, 2, 6),
    (2, 10, 6, 10, 4, 15, 3, 11),
    (3, 14, 8, 9, 6, 12, 8, 1),
    (14, 7, 5, 14, 12, 7, 1, 12),
    (6, 6, 9, 0, 11, 6, 0, 7),
    (11, 8, 12, 3, 2, 0, 7, 15),
    (8, 2, 15, 11, 5, 9, 5, 5),
    (12, 12, 14, 2, 3, 11, 9, 3),
)

text = str(input("Введите текст: "))[:12]
if len(text) < 12:
    print("Применено автозаполнение")
    text = text.ljust(12, " ")
print(text)
print()
bintext = ""

for i in text:
    bintext += binary(i)
    bintext += " "
bintext = bintext[:8 * 12 + 11]

L0 = bintext[:8 * 4 + 3]
R0 = bintext[8 * 4 + 4:8 * 8 + 7]
X = bintext[8 * 8 + 8:]

print("Бинарная запись: ", bintext)
print()
print("L0: ", L0)
print()
print("R0: ", R0)
print()
print("X: ", X)
print()
summa = sum_binary_strings(X, R0)
print("Сумма R0 + X: ", summa)
print()

list_num1 = list(range(8, 0, -1))  #Столбцы таблицы
list_num2 = list()  #десятичная запись числа + строки таблицы
list_bin1 = list()  #сумма r0+x
list_bin2 = list()  #значения из таблицы в двоичную запись
group = ""  #временно для двоичного числа хххх

#print(list_num1)

for i in range(len(summa)):
    if summa[i] != " ":
        group += summa[i]
        if len(group) == 4:
            list_bin1.append(group)
            list_num2.append(binary_to_decimal(int(group)))
            group = ""

print(list_bin1)
print()
print("В десятичной записи: ", list_num2)
print()

list_num3 = list()  #значение  из таблицы десятичное
# noinspection PyRedeclaration
list_num3, list_bin2 = search_table(table, list_num2, list_num1)

print("Значения из таблицы: ", list_num3)
print()
print("В двоичной записи: ", list_bin2)
print()

pred_f = "".join(list_bin2)  #из списка в строку
f = shift_string(pred_f, 11)
print("f:", f)
print()
R1 = calculate_module2(f, L0)
print("Ответ:")
print("R1: ", R1)

# list_R1=list()
# for i in range(len(R1)):
#     if R1[i] != " ":
#         group += R1[i]
#         if len(group) == 4:
#             list_R1.append(group)
#             group = ""
# print("Ответ: ",list_R1)

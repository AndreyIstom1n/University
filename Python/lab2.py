#Операции P, R, I
n = int(input("Количество товаров на складе: "))
t = {}
while n != 0:
    name, *oper = input("Введите товар и операции: ").split()
    t[name] = oper
    n -= 1
print(t, "\n")
m = int(input("Количество запросов по товарам: "))
while m != 0:
    oper, name = input("Введите операцию и товар: ").split()
    if oper == "P":
        if "P" in t[name]:
            print("OK")
        else:
            print("Acces denied")
    elif oper == "R":
        if "R" in t[name]:
            print("OK")
        else:
            print("Acces denied")
    elif oper == "I":
        if "I" in t[name]:
            print("OK")
        else:
            print("Acces denied")
    print('')
    m -= 1

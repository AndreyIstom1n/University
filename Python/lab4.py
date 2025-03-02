class Client:
    def __init__(self, code, FIO, OpDep, AmoDep, IntDep):
        self.code = code  # код клиента
        self.FIO = FIO  # фио
        self.OpDep = OpDep  # дата открытия вклада
        self.AmoDep = AmoDep  # размер вклада
        self.IntDep = IntDep  # процент по вкладу

    def __str__(self):
        print("Информация о клиенте: ")
        return f'Код: {self.code}, ФИО: {self.FIO}, дата открытия вклада: {self.OpDep}, размер вклада: {self.AmoDep}, процент по вкладу: {self.IntDep}'


class Bank:
    def __init__(self):
        clientBase = []
        self.clientBase = clientBase

    def addClient(self, client):
        self.clientBase.append(client)

    def showBy(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

        return wrapper

    @showBy
    def showByMoney(self, money):
        for client in self.clientBase:
            if client.AmoDep > money:
                print(f"Клиент {client.FIO}, у которого размер вклада больше {money}")

    @showBy
    def showByCode(self, code):
        for client in self.clientBase:
            if client.code == code:
                print(f"Искомый клиент с кодом {code}:")
                print(client)  # использование __str__

    @showBy
    def showByProc(self, proc):
        for client in self.clientBase:
            if client.IntDep > proc:
                print(f"Клиент {client.FIO}, у которого процент по вкладу больше {proc}")


bank = Bank()
bank.addClient(Client(1, 'Истомин Андрей Викторович', '18.04.2024', 1599, 7))
bank.addClient(Client(2, 'Иванов Пётр Александрович', '01.03.2000', 1700, 15))
bank.addClient(Client(3, 'Петров Александр Иванович', '03.01.1953', 5000, 10))
'''
a1=Client(4, 'Александров Иван Петрович', '10.06.2004', 6000,2)
print (a1)
print()
'''
bank.showByMoney(1800)
print()
bank.showByCode(1)
print()
bank.showByProc(12)

"""
n=int(input("Количество клиентов: "))
for x in range (n):
    print("Клиент № ",x+1)
    fio=str(input("FIO: "))
    date=str(input("Дата: "))
    vklad=int(input("Размер вклада: "))
    proc=int(input("Процент по вкладу: "))
    bank.addClient(Client(x+1,fio,date,vklad,proc))
    print()
money=int(input("Задать размер вклада: "))
code=int(input("Искать по коду: " ))
procent=int(input("Задать процент по вкладу: "))
print()
bank.showByMoney(money)
print()
bank.showByCode(code)
print()
bank.showByProc(procent)
"""

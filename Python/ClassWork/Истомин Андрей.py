"""s=input('Введите')
#s=input()
#h=int(input())
#print(s,h)

#if a=b:
#    a-b
#elif a=c:
#    a+c
#else:
#    a/10

"""



#№1
""" #1
n=int(input('Введите n:'))
b=int(0)
v=int(0)
#print(n)

v=n//60//24 #часы
b=n%60 #минуты

print('Часы: ',v,' ','Минуты: ',b)
"""

"""#2
n=int(input('Введите количество школьников: '))
k=int(input('Введите количество яблок: '))
x=int((k%n))
otvet=int(n-x)
print(otvet," Детей получит яблок меньше, чем некоторые")
"""

"""#3
n=int(input('Введите число n: '))
print((n//2+1)*2)
"""

"""#4
m=int(input("Введите m расстояние: "))
n=int(input("Введите n скорость машины: "))
x=int(m/n)
c=int(m%n)
c/=c
res=int(x+c)
print(res)
"""

#№2
""" #1
n=int(input("Введите количество требуемых кусков: "))
if(n%2!=0):
    print("Необходимо ",n, " разрезов")
elif(n%2==0):
    print("Необходимо ",n//2, " разрезов")
"""
#2 - ???

"""№3 #1 - ????
a=int(input("Введите число А: "))
b=int(input("Введите число В: "))
for i in range (a,b+1,2):
    print (i)
"""
""" #3 - ????
n=int(input("Введите n: "))
fib=int(1)
x=int(1)
z=int(1)
for i in range(2,n+1):
    fib+=i*z+x
    x+=1
    z*=x-1
print(fib)
"""

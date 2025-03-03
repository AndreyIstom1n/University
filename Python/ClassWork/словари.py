#1
"""my=input().split()
a=dict()
for i in my:
    if(i in a.keys()):
        a[i]+=1
    else:
        a[i]=0
    print(a[i])
"""
#2
"""
a=input().split()
b=dict()
max=0
for i in a:
    if(i in b.keys()):
        b[i]+=1
    else:
        b[i]=1
    if b[i]>max:
        max=b[i]
c=sorted(b)
for i in b.keys():
    if b[i]==max:
        print(i)
        break
"""
#3
"""
n=int(input("Количество слов: "))
a={}
while n!=0:
    key,value=input().split()
    a[key]=value
    n-=1
print(a)
b=input("Поиск: ")
if b in a.keys():
    print(a[b])
elif b in a.values():
    for key in a.keys():
        if a[key]==b:
            print(key)
else:print("Синонимов нет")
"""
#4
n=int(input("Количество слов: "))
a={}
while n!=0:
    key,value=input().split()
    a[key]=value
    n-=1
c={}
c=sorted(a)
print(c.items())

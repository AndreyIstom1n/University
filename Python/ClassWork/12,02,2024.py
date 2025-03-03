#1
"""a=list(map(int,input().split()))
for i in range(0,len(a),2):
    print(a[i])
"""

#2
"""a=list(map(int,input().split()))
b=[x for x in a if x%2==0]
    print(b)
"""
#3
"""k=int(0)
a=list(map(int,input().split()))
for i in range(1,len(a)-1):
    if(a[i]>a[i-1]and a[i]>a[i+1]):
        k+=1
print(k)
"""
#4
sum=int(0)
a=list(map(int,input().split()))
kol=int(len(a))
for i in range(0,len(a)-1):
    if(a[i]==2 and a[i+1]!=2):
        sum+=0
        kol-=1
    else:
        sum+=a[i]
for i in range(len(a)):
    if(i==(len(a)-1)):
        sum+=a[i]
sr=int(sum//kol)
print(sr)

#8
a=list(map(int,input().split()))
minim=int(a[0])
maxim=int(a[0])
for i in range(1,len(a)):
    if (a[i]<=a[i-1]):
        min=a[i]
    elif (a[i]>=a[i-1]):
        max=a[i]
  

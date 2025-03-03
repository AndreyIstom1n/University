#1
#num={1,2,3,4,3,2,1}
#print(set(num))

#2
"""
num1={1,2,3,4,5,8,7,6}
num2={6,7,8,9,0}
print(sorted(num1.intersection(num2)))
"""
#3
"""
x=input().split()
n=set()
for i in x:
    if i in n:
        print("Yes")
    else:print("No")
    n.add(i)
"""
#4
"""
x={'green', 'red', 'blue'}
y={'red', 'yellow','green'}
print(len(x.union(y)),"Vsego")
print(x|y)
print(len(x.difference(y)), "U pervogo")
print(x-y)
print(len(y.difference(x)), "U vtorogo")
print(y-x)
"""
#5
n = int(input)
x = set(input().split())
s = x
s2 = x
for i in range(n-1):
    x=set(input().split())
    


#1.1
"""s=str(input())
print(s[:5])
"""
#1.2
"""s=str(input())
print(s[:len(s)-2])
"""
#1.3
"""s=str(input())
print(s[1:len(s):2])
"""
#1.4
"""s=str(input())
print(s[::-2])
"""
#2
"""s=str(input())
print(s.count(" ")+1)
"""
#3
'''
s=str(input())

s = s.replace('','*')
print(s[1:len(s)-1])
'''
"""
a=str(" ")
for i in range(0,len(s)-1):
    a+=s[i]+"*"
a+=s[len(s)-1:len(s)]
print(a)
"""
#4
'''
s=str(input())
a=str(" ")
s=s.strip()
print(s)
'''


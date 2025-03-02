# input,input2,input3
#inp = open('lab3/input.txt', 'r', encoding='utf8')
#inp = open('lab3/input2.txt', 'r', encoding='utf8')
inp = open('lab3/input3.txt', 'r', encoding='utf8')
outp = open('lab3/output.txt', 'w', encoding='utf8')

k = inp.readline()
k = int(k)
l = str(inp.readlines())

res = []
summa = 0
c = 0
flag = 0
lgt = len(l)
num = []
i = 0

while i < lgt:
    s_int = ''
    while i < lgt and '0' <= l[i] <= '9':
        s_int += l[i]
        i += 1
    i += 1
    if s_int != '':
        num.append(int(s_int))

for i in num:
    if int(i) < 40:
        summa += int(i)
        c += 1
        flag = 1
    else:
        summa += int(i)
        c += 1
    if c == 3 and flag == 0:
        res.append(summa)
        c = 0
        summa = 0
    elif c == 3 and flag == 1:
        res.append(0)
        c = 0
        summa = 0
        flag = 0

res.sort(reverse=True)
if res[k] == 0:
    outp.write(str(0))
elif res[0] == res[k]:
    outp.write(str(1))
elif res[k] == res[k - 1]:
    outp.write(str(res[k - 2]))

else:
    outp.write(str(res[k - 1]))

inp.close()
outp.close()

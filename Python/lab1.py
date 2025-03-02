#Ввод: строка из цифр 1-9. Заканчивается точкой. Вывод: Цифры, отсутствующие в строке
s = str("")
k = str(input())
s += k

while s[-1] != ".":
    k = input()
    s += k

x = set()
y = str("")

for i in range(1, 10):
    if str(i) not in s:
        x.add(i)
if not x:
    print(0)
z = set()
z = sorted(x)
for i in z:
    y += str(i)
print(y)

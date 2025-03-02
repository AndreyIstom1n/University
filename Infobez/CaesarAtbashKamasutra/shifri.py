import string
import random
def caes():
    print()
    print("Шифр Цезаря")
    res=""
    text=input("Введите текст: ")
    key=int(input("Введите ключ: "))
    for i in text:
            if 'А' <= i <= 'Я':
                step = chr((ord(i) - ord('А') + key) % 32 + ord('А'))
                res += step
            elif 'а' <= i <= 'я':
                step = chr((ord(i) - ord('а') + key) % 32 + ord('а'))
                res += step
            elif 'A' <= i <= 'Z':
                step = chr((ord(i) - ord('A') + key) % 26 + ord('A'))
                res += step
            elif 'a'<= i <= 'z':
                step = chr((ord(i) - ord('a') + key) % 26 + ord('a'))
                res += step
            else:
                res += i
    print("Зашифрованный текст: "+res)
    return decaes(res,key)
def decaes(text,key):
    new_res=""
    for i in text:
        if 'А' <= i <= 'Я':
            step = chr((ord(i) - ord('А') - key) % 32 + ord('А'))
            new_res += step
        elif 'а' <= i <= 'я':
            step = chr((ord(i) - ord('а') - key) % 32 + ord('а'))
            new_res += step
        elif 'A' <= i <= 'Z':
            step = chr((ord(i) - ord('A') - key) % 26 + ord('A'))
            new_res += step
        elif 'a'<= i <= 'z':
            step = chr((ord(i) - ord('a') - key) % 26 + ord('a'))
            new_res += step
        else:
            new_res += i
    print("Расшифрованный текст: "+new_res)
    print()
    return choose_function()
            
def kama():
    print()
    print("Шифр Камасутра")
    alph_lower = [chr(i) for i in range(ord('а'), ord('я')+1)]
    alph_upp = [chr(i) for i in range(ord('А'), ord('Я')+1)]
    x = ''.join(alph_lower)
    y = ''
    for i in range(int(len(x)/2)):
        r = random.randint(0, len(x)-1)
        y += x[r]
        x = x.replace(x[r], "", 1)
    key_lower = list(y)
    alph_lower1 = list(x)
    print("Ключ")
    print(alph_lower1)
    print(key_lower)
    print()
    c = ''.join(alph_upp)
    v = ''
    for i in range(int(len(c)/2)):
        r = random.randint(0, len(c)-1)
        v += c[r]
        c = c.replace(c[r], "", 1)
    key_upp = list(v)
    alph_upp1 = list(c)
    print(alph_upp1)
    print(key_upp)
    text=input("Введите текст (rus): ")
    text_list=list(text)
    for j in range(len(text_list)):
       if text_list[j] in alph_lower1:
           i = alph_lower1.index(text_list[j])
           text_list[j] = key_lower[i]
       elif text_list[j] in key_lower:
           i = key_lower.index(text_list[j])
           text_list[j] = alph_lower1[i]
       elif text_list[j] in alph_upp1:
           i = alph_upp1.index(text_list[j])
           text_list[j] = key_upp[i]
       elif text_list[j] in key_upp:
           i = key_upp.index(text_list[j])
           text_list[j] = alph_upp1[i]
    print("Зашифрованный текст: ")
    print(''.join(text_list))
    for j in range(len(text_list)):
        if text_list[j] in alph_lower1:
            i = alph_lower1.index(text_list[j])
            text_list[j] = key_lower[i]
        elif text_list[j] in key_lower:
            i = key_lower.index(text_list[j])
            text_list[j] = alph_lower1[i]
        elif text_list[j] in alph_upp1:
            i = alph_upp1.index(text_list[j])
            text_list[j] = key_upp[i]
        elif text_list[j] in key_upp:
            i = key_upp.index(text_list[j])
            text_list[j] = alph_upp1[i]
    print("Расшифрованый текст: ")
    print(''.join(text_list))
    print()
    return choose_function()     
def atbash():
    print()
    print("Шифр AtBash")
    res=""
    text=input("Введите текст: ")
    for i in text:
        if i.isalpha():
            if 'A'<=i<='Z' or 'a'<=i<='z':
                base = ord('A') if i.isupper() else ord('a')
                encrypted_char = chr(base + (25 - (ord(i) - base)))
                res += encrypted_char
            elif 'А'<=i<='Я' or 'а'<=i<='я':
                base = ord('А') if i.isupper() else ord('а')
                encrypted_char = chr(base + (31 - (ord(i) - base)))
                res += encrypted_char    
        else:
            res += i
    print("Зашифрованный текст: "+res)
    return deatbash(res)

def deatbash(text):
    new_res=''
    for i in text:
        if i.isalpha():
            if 'A'<=i<='Z' or 'a'<=i<='z':
                base = ord('A') if i.isupper() else ord('a')
                encrypted_char = chr(base + (25 - (ord(i) - base)))
                new_res += encrypted_char
            elif 'А'<=i<='Я' or 'а'<=i<='я':
                base = ord('А') if i.isupper() else ord('а')
                encrypted_char = chr(base + (31 - (ord(i) - base)))
                new_res += encrypted_char    
        else:
            new_res += i
    print("Расшифрованный текст: "+new_res)
    print()
    return choose_function()




def choose_function():
    options = [caes, kama, atbash]
    print("Выберите одну из функций:")
    print("1. Шифр Цезаря")
    print("2. Шифр Камасутра")
    print("3. Шифр AtBash")
    print("4. Выход")
    choice = int(input("Введите номер функции (1-4): "))

    if choice < 1 or choice > 4:
        print("Некорректный выбор. Попробуйте снова.")
        print()
        return
    elif choice == 4:
        return exit()
    selected_function = options[choice - 1]
    selected_function()

while 1>0:
    choose_function()
print("Завершение работы")

"""Вариант 6 Дан файл в формате csv. (Фамилия, Имя, Учреждение (организация), Отдел, Адрес электронной почты,
Состояние, Тест начат, Завершено, Затраченное время, Оценка/100,00, В.1 /10,00, В.2 /10,00, В.3 /10,00, В.4 /10,00,
В.5 /10,00, В.6 /10,00, В.7 /10,00, В.8 /10,00, В.9 /10,00, В.10 /10,00). Примечание: Тест считается пройденным,
если набрано 6/10 (60/100) баллов. Примечание: Поля «Тест начат», «Завершено» заданы в формате «12 Май 2017 10:09»,
поле «Затраченное время» в формате «31 мин. 22 сек.». Найти количество людей, фамилии которых начинаются с заданной
буквы, которые прошли тест раньше заданной даты. Вывести их список.."""
import csv
from datetime import datetime
import locale


def convert_to_float(value):
    try:
        return float(value.replace(',', '.'))
    except ValueError:
        return None


locale.setlocale(locale.LC_TIME, 'ru')
date_string = '12 Апрель 2017  22:00'
date_object = datetime.strptime(date_string, '%d %B %Y  %H:%M')
target_letter = 'К'

with (open('lab7/6 - 1.csv', newline='', encoding='utf-8') as csv_file):
    reader = csv.reader(csv_file)
    next(reader)
    count = 0
    for row in reader:
        last_name = row[0]
        value_6 = row[6]
        if value_6 != '':
            end_date = datetime.strptime(row[6], '%d %B %Y  %H:%M')
            value_9 = row[9]
            if value_9 != '-' and last_name.startswith(target_letter) and end_date != '-' and end_date < date_object:
                value_9_float = convert_to_float(value_9)
                if value_9_float is not None and value_9_float >= 6:
                    count += 1
                    print(f'{last_name},{row[1]}')

print(f'Всего людей в первом файле: {count}')
print()

locale.setlocale(locale.LC_TIME, 'ru')
date_string = '20 Май 2017  18:00'
date_object = datetime.strptime(date_string, '%d %B %Y  %H:%M')
target_letter = 'Р'

with (open('lab7/6 - 2.csv', newline='', encoding='utf-8') as csv_file):
    reader = csv.reader(csv_file)
    next(reader)
    count = 0
    for row in reader:
        last_name = row[0]
        value_6 = row[6]
        if value_6 != '':
            end_date = datetime.strptime(row[6], '%d %B %Y  %H:%M')
            value_9 = row[9]
            if value_9 != '-' and last_name.startswith(target_letter) and end_date != '-' and end_date < date_object:
                value_9_float = convert_to_float(value_9)
                if value_9_float is not None and value_9_float >= 6:
                    count += 1
                    print(f'{last_name},{row[1]}')

print(f'Всего людей во втором файле: {count}')

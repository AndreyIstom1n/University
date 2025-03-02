import sqlite3

con = sqlite3.connect("db01.db")
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS dance')
cur.execute('DROP TABLE IF EXISTS dancer')
cur.execute('DROP TABLE IF EXISTS mentor')
cur.execute('DROP TABLE IF EXISTS action')
cur.execute('DROP TABLE IF EXISTS dance_mentor')
cur.execute('DROP TABLE IF EXISTS place')
cur.execute('DROP TABLE IF EXISTS event')

cur.execute('''CREATE TABLE IF NOT EXISTS dance(
            id_dance INTEGER PRIMARY KEY,
            type VARCHAR(30) NOT NULL,
            level INTEGER
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS dancer(
            id_dancer INTEGER PRIMARY KEY,
            name_d VARCHAR(30) NOT NULL,
            gender VARCHAR(30) NOT NULL,
            phone VARCHAR(30) NOT NULL,
            level_d INTEGER
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS mentor(
            id_mentor INTEGER PRIMARY KEY,
            name_m VARCHAR(30) NOT NULL,
            phone VARCHAR(30) NOT NULL,
            exp INTEGER
            )''')
cur.execute('''CREATE TABLE IF NOT EXISTS place(
            id_place INTEGER PRIMARY KEY,
            address VARCHAR(30) NOT NULL
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS action(
            id_action INTEGER PRIMARY KEY,
            id_dance INTEGER,
            type VARCHAR(30) NOT NULL,
            id_dancer INTEGER,
            name_d VARCHAR(30) NOT NULL,
            id_mentor INTEGER,
            name_m VARCHAR(30) NOT NULL
            )''')
cur.execute('''CREATE TABLE IF NOT EXISTS dance_mentor(
            id_dm INTEGER PRIMARY KEY,
            id_dance INTEGER,
            type VARCHAR(30) NOT NULL,
            id_mentor INTEGER,
            name_m VARCHAR(30) NOT NULL,
            level INTEGER
            )''')
cur.execute('''CREATE TABLE IF NOT EXISTS event(
            id_event INTEGER PRIMARY KEY,
            id_action INTEGER,
            id_place INTEGER,
            address VARCHAR(30) NOT NULL,
            start VARCHAR (30) NOT NULL,
            end VARCHAR (30) NOT NULL
            )''')

con.commit()

command = '''
        INSERT INTO dance
        VALUES(1, 'Танго', 3);'''
cur.execute(command)
command = '''
        INSERT INTO dance
        VALUES(2, 'Спортивные танцы', 1);'''
cur.execute(command)
command = '''
        INSERT INTO dance
        VALUES(3, 'Вальс', 2);'''
cur.execute(command)

command = '''
        INSERT INTO dancer
        VALUES(1, 'Olga','Female','+79813233838', 2);'''
cur.execute(command)
command = '''
        INSERT INTO dancer
        VALUES(2, 'Vasiliy','Male','+72326561212', 1);'''
cur.execute(command)
command = '''
        INSERT INTO dancer
        VALUES(3, 'Aleksandra','Female','+75252525252', 3);'''
cur.execute(command)

command = '''
        INSERT INTO mentor
        VALUES(1, 'Anastasiya Andreevna','+71234567890', 8);'''
cur.execute(command)
command = '''
        INSERT INTO mentor
        VALUES(2, 'Evgeniy Anatolievich','+70987654321', 4);'''
cur.execute(command)
command = '''
        INSERT INTO mentor
        VALUES(3, 'Ekaterina Viktorovna','+79642315467', 15);'''
cur.execute(command)
command = '''
        INSERT INTO place
        VALUES(1, 'ул.Ставропольская 101');'''
cur.execute(command)
command = '''
        INSERT INTO place
        VALUES(2, 'ул.Тургенева 12');'''
cur.execute(command)
command = '''
        INSERT INTO place
        VALUES(3, 'ул.Гагарина 52');'''
cur.execute(command)

command = '''
        INSERT INTO action
        VALUES(1,3,'Вальс',3,'Aleksandra',1,'Anastasiya Andreevna');'''
cur.execute(command)
command = '''
        INSERT INTO action
        VALUES(2,1,'Танго',3,'Aleksandra',3,'Ekaterina Viktorovna');'''
cur.execute(command)
command = '''
        INSERT INTO action
        VALUES(3,2,'Спортивные танцы',2,'Vasiliy',2,'Evgeniy Anatolievich');'''
cur.execute(command)

command = '''
        INSERT INTO dance_mentor
        VALUES(1,1,'Танго',3,'Ekaterina Viktorovna',3);'''
cur.execute(command)
command = '''
        INSERT INTO dance_mentor
        VALUES(4,3,'Вальс',3,'Ekaterina Viktorovna',3);'''
cur.execute(command)
command = '''
        INSERT INTO dance_mentor
        VALUES(2,2,'Спортивные танцы',2,'Evgeniy Anatolievich',1);'''
cur.execute(command)
command = '''
        INSERT INTO dance_mentor
        VALUES(3,3,'Вальс',1,'Anastasiya Andreevna',2);'''
cur.execute(command)
command = '''
        INSERT INTO event
        VALUES(1,2,2,'ул.Тургенева 12','15:30','17:00');'''
cur.execute(command)
command = '''
        INSERT INTO event
        VALUES(2,3,1,'ул.Ставропольская 101','12:45','15:00');'''
cur.execute(command)
command = '''
        INSERT INTO event
        VALUES(3,1,3,'ул.Гагарина 52','17:30','20:00');'''
cur.execute(command)
con.commit()

cur.execute('SELECT * FROM dance;')
columns = cur.fetchall()
print("Танцы. Количество видов: ", len(columns))
print("\nВиды танцев: ")
for row in columns:
    print("\nID: ", row[0])
    print("Вид: ", row[1])
    print("Необходимый уровень: ", row[2])

cur.execute('SELECT action.id_dance, action.type, action.name_d, dancer.name_d from action,dancer WHERE '
            'dancer.name_d=="Aleksandra"and dancer.name_d==action.name_d')
columns = cur.fetchall()
print("\nЗанятия, на которое записана Aleksandra: ")
for row in columns:
    print("\nID танца: ", row[0])
    print("Вид танца: ", row[1])

cur.execute('SELECT dance_mentor.id_dance,dance_mentor.type,dance_mentor.id_mentor,dance_mentor.name_m, '
            'mentor.id_mentor,mentor.name_m,mentor.exp,mentor.phone from dance_mentor,mentor WHERE '
            'dance_mentor.type=="Вальс" and '
            'dance_mentor.id_mentor==mentor.id_mentor')
columns = cur.fetchall()
print("\nТренеры, преподающие вальс: ")
for row in columns:
    print("\nID тренера: ", row[4])
    print("Имя: ", row[5])
    print("Стаж работы: ", row[6])
    print("Номер телефона: ", row[7])
con.close()
import sqlite3
con=sqlite3.connect("db01.db")
cur=con.cursor()
cur.execute('DROP TABLE IF EXISTS tourism') 
cur.execute('''CREATE TABLE IF NOT EXISTS tourism(
            id INTEGER PRIMARY KEY,
            action VARCHAR(30),
            mentor VARCHAR(30)
            )''')
cur.execute('''CREATE TABLE IF NOT EXISTS tourists(
            id INTEGER PRIMARY KEY,
            name VARCHAR(30),
            gender VARCHAR(30)
            )''')

var_list=[
    (1,"Driving","Ivan"),
    (2,"Swimming","Oleg"),
    (3,"Chilling","Andrey")]
sql='''\
    INSERT INTO tourism(id,action,mentor)
    VALUES (?,?,?)
    '''
cur.executemany(sql,var_list)
con.commit()
print(cur.lastrowid)
cur.execute('SELECT * FROM tourism')
print(cur.fetchall())
con.close()

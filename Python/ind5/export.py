import sqlite3
import xml.dom.minidom
from sqlite3 import Connection

conn: Connection = sqlite3.connect('db01.db')
cursor = conn.cursor()
xml_file = 'dancer.xml'
doc = xml.dom.minidom.parse(xml_file)
dancers = doc.getElementsByTagName('record')

for dancer in dancers:
    id_dancer = int(dancer.getElementsByTagName('id_dancer')[0].firstChild.nodeValue)
    name_d = dancer.getElementsByTagName('name_d')[0].childNodes[0].data
    gender = dancer.getElementsByTagName('gender')[0].childNodes[0].data
    phone = dancer.getElementsByTagName('phone')[0].childNodes[0].data
    level_d = dancer.getElementsByTagName('level_d')[0].childNodes[0].data
    print(id_dancer, name_d, gender, phone, level_d)
    cursor.execute("INSERT OR IGNORE INTO dancer (id_dancer, name_d, gender, phone, level_d) VALUES(?, ?, ?, ?, ?)",(id_dancer, name_d, gender, phone, level_d))
conn.commit()
conn.close()
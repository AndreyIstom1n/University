import sqlite3 as sql
import xml.dom.minidom

connection = sql.connect("db01.db")
doc = xml.dom.minidom.Document()
root = doc.createElement('table')
doc.appendChild(root)

dancers_table_fields = ['id_dancer', 'name_d', 'gender', 'phone','level_d']

dancers = connection.cursor().execute('SELECT * FROM dancer').fetchall()
for row in dancers:
    record = doc.createElement('record')
    root.appendChild(record)
    for _i in range(len(dancers_table_fields)):
        element = doc.createElement(dancers_table_fields[_i])
        element.appendChild(doc.createTextNode(str(row[_i])))
        record.appendChild(element)

with open('dancer.xml', 'w') as f:
    f.write(doc.toprettyxml())
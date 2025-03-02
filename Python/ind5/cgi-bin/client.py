import cgi
form = cgi.FieldStorage()
text1 = form.getfirst("name", "TBD")
text2 = form.getvalue("gender", "TBD")
text3 = form.getfirst("phone", "TBD")
text4 = form.getvalue("level_d", "TBD")
print("Content-type: text/html\n")
print('''<!DOCTYPE HTML>
         <html lang="en">
         <head>
            <meta charset="UTF-8">
            <title>Client information</title>
        </head>
        <body>''')
print("<h1>Client</h1>")
print("<p>Name: {}</p>".format(text1))
print("<p>Gender: {}</p>".format(text2))
print("<p>Phone: {}</p>".format(text3))
print("<p>Level: {}</p>".format(text4))
print("""</body>
</html>""")
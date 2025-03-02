import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("name_m", "TBD")
text2 = form.getvalue("phone_m", "TBD")
text3 = form.getfirst("exp", "TBD")
print("Contet-type: text/html\n")
print('''<!DOCTYPE HTML>
         <html lang="en">
         <head>
            <meta charset="UTF-8">
            <title>Client information</title>
        </head>
        <body>''')
print("<h1>Mentor</h1>")
print("<p>Name: {}</p>".format(text1))
print("<p>Phone: {}</p>".format(text2))
print("<p>Experience: {}</p>".format(text3))
print("""</body>
</html>""")
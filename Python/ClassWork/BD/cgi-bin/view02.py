import cgi
form = cgi.FieldStorage()
text1=form.getfirst("mentor","TBD")
text2=form.getfirst("action","TBD")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
    <head>
     <meta charset="cp1251">
     <title>Connection</title>
    </head>
    <body>""")
print("<h1>Connection</h1>")
#print("<p>Mentor:{}</p>".format(text1))
#print("<p>Action:{}</p>".format(text2))
print("<p>Mentor: %s</p>"%text1)
print("<p>A : %s</p>"%text2)
print("""</body> </html>""")

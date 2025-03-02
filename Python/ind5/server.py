from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

server_address = ("", 8000)
httpd_server = HTTPServer(server_address, CGIHTTPRequestHandler)
print("Start: http://localhost:8000/form.html")
httpd_server.serve_forever()

from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler
server_address=("",8000)
http_server=HTTPServer(server_address, CGIHTTPRequestHandler)
http_server.serve_forever()

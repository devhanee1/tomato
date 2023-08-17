import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler
port_num = 8000

with socketserver.TCPServer(('', port_num), handler) as httpd:
    print('Server listening on port ', port_num)
    httpd.serve_forever()

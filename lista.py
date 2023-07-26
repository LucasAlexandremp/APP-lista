from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 5500

handler = SimpleHTTPRequestHandler
httpd = HTTPServer(('0.0.0.0', PORT), handler)

print(f'Servidor iniciado na porta {5500}. Acesse http://localhost:{5500}')
httpd.serve_forever()

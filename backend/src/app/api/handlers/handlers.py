from http.server import BaseHTTPRequestHandler
from ....core.services import Services

class Handlers(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/load_data":
            data = Services().loadAll()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(data.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'P\xc3\xa1gina n\xc3\xa3o encontrada')

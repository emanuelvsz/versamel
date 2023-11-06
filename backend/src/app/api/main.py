import http.server
import socketserver
from handlers import Handlers

# Porta na qual o servidor irá ouvir
PORT = 8000

# Crie um manipulador personalizado para as solicitações
handler = Handlers()

# Inicialize o servidor
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Servidor rodando na porta", PORT)
    httpd.serve_forever()

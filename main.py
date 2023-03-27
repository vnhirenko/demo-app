from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import socket 
from requests import get

class HttpProcessor(BaseHTTPRequestHandler):

    def do_GET(self):
        self.myget()

    def saveHeaders(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def myget(self):
        if self.path == '/':
            self.saveHeaders()
            self.wfile.write(bytes('hello from demo app!', 'utf-8'))
        elif self.path == '/getIP':
            extIP = get('https://api.ipify.org').content.decode('utf8')
            ipAddr=socket.gethostbyname(socket.gethostname())
            self.saveHeaders()
            self.wfile.write(bytes(f"Internal: {ipAddr}!\nExternal: {extIP}\n", 'utf-8'))
        elif self.path == '/getHost':
            hostname=socket.gethostname() 
            self.saveHeaders()
            self.wfile.write(bytes(f"Hello! My Hostname is {hostname}!", 'utf-8'))
        else:
            self.send_error(404,'there is no such a page')

def run(host='0.0.0.0', port=8080, server_class=HTTPServer, handler=HttpProcessor):
    server_address = (host, port)
    httpd = server_class(server_address, handler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()

if __name__ == "__main__": 
    run()

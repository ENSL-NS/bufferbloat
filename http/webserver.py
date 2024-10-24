import SimpleHTTPServer
import SocketServer

class WebServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    # Disable logging DNS lookups
    def address_string(self):
        return str(self.client_address[0])


PORT = 8080

Handler = WebServerHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print("Server1: httpd serving at port", PORT)
httpd.serve_forever()

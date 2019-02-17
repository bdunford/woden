from http.server import BaseHTTPRequestHandler,HTTPServer
from ..utility import Printer

class Listener(object):

    @staticmethod
    def Listen(port,callback=None):
        try:
            callback = callback if callback else _callback
            server = HTTPServer(('', port),RequestHandler)
            server.RequestHandlerClass.callback = callback
            server.serve_forever()

        except KeyboardInterrupt:
	        print('^C received, shutting down the web server')
	        server.socket.close()

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self._respond()
        return

    def do_DELETE(self):
        self.do_GET()

    def do_POST(self):
        content = self.rfile.read(int(self.headers.getheader('content-length', 0)))
        self._respond(content)
        return

    def do_PATCH(self):
        self.do_POST()
    
        
    def _parse(self,estring):
        parts = estring.split('?')
        v = parts[1] if len(parts) > 1 else parts[0]
        pairs = qs.split("&")
        results = {}
        for p in pairs: 
            kv = p.split("=")
            if len(kv) > 0:
                results[kv[0]] = kv[1] if len(kv) > 1 else ""
        return results

    def _respond(self,content=""):
        self.callback(content)

def _callback(self,content=""):
    Printer.HR()
    print("Remote: %s" % self.address_string())
    print("Path: %s" % self.path)
    print("=====HEADERS=====")
    Printer.Print(dict(self.headers))
    print("=====QUERY=======")
    Printer.Print(self._parse(self.path))
    print("=====BODY========")
    Printer.Print(content)
    print("=====SUMMARY=====")
    
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write("<html><p>lol</p></html>")

"""
import woden
from woden.web import Listener
def x(self,log):
    print log
Listener.Listen(8181,x)

OR

import woden
from woden.web import Listener
Listener.Listen(8181)

"""

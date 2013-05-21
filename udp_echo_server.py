"UASAGE : %s<port>"
from SocketServer import DatagramRequestHandler, UDPServer
from sys import argv

class EchoHandler(DatagramRequestHandler):
    def handle(self):
        print "client connected:", self.client_address
        message = self.rfile.read()
        self.wfile.write(message)


if len(argv) != 2:
    print __doc__ % argv[0]
else:
    UDPServer(('',int(argv[1])), EchoHandler).serve_forever()

"USaGE: %s <server> <word> <port>"
from SocketServer import DatagramRequestHandler, UDPServer
from sys import argv
if len(argv) != 4:
    print __doc__ % argv[0]
    exit(0)
sock=socket(AF_INET, SOCK_DGRAM)
messout = argv[2]
sock.sendto(messout, (argv[1], int(argv[3])))
messin, server = sock.recvfrom(255)
if messin != messout:
    print "failed to receive identical message"
print "received:", messin
sock.close()

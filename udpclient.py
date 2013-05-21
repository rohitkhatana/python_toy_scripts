import socket
clisock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


clisock.sendto( "hello world\n", ('192.168.188.131',12000) )
print clisock.recv( 100 )
clisock.close()

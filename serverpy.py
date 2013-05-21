import socket
#server
socserv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socserv.bind( ('',23000) )
socserv.listen(5)
while 1:
    clisock, (remotehost,remoteport) = socserv.accept()
    str = clisock.recv(100)
    clisock.send('rohit\n')
    clisock.close()
                      
                      

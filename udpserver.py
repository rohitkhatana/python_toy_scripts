import socket
servsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#datagram(UDP)echo server
servsock.bind( ('',12000) )
while 1:
    msg, (remhost,remport) = servsock.recvfrom( 100 )
    print msg
    servsock.sendto(msg, (remhost,remport))
    

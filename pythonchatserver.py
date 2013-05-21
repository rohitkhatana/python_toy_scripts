import socket
import select

class ChatServer:
    def __init__(self, port ):
        self.port = port;

        self.sevsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsock.setsockopt( socket.SOL_SOCKET, socket.so_REUSEADDR, 1 )
        self.srvsock.bind( ("",port) )
        self.srvsock.listen( 5 )

        self.descriptors = [self.srvsock]
        print 'chatserver started on port %S' % port

    def run( self ):

        while 1:
            (sread, swrite, sexc) = select.select( self.descriptors, [], [] )
            for sock in sread:
                if sock == self.srvsock:
                    self.accept_new_connection()
                else:
                    str1=sock.recv(100)

                    if str1== '':
                        host,port = sock.getpeername()
                        self.broadcast_string( str, sock )
                        sock.close
                        self.descriptors.remove(sock)
                    else:
                        host,port = sock.getpeername()
                        newstr1= '[%s:%s] %s' % (host,port, str1)
                        self.broadcast_string( newstr, sock)


    def accept_new_connection( self ):
        newsock, (remhost, remport) =self.srvscok.accept()
        self.descriptors.append( newsock )
        newsock.send("you're connected to the python chatserver\r\n")
        str1= 'Client joined %s:%s\r\n' % (remhost, remport)
        self.broadcast_string( str1, newsock )


    def broadcast_string( self, str1, omit_sock ):
        for sock in self.descriptors:
            for sock in self.descriptors:
                if sock != self.srvsock and sock != omit_sock:
                    sock.send(str1)

            print str1
            

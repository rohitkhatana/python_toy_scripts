import socket
clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clisock.connect( ('192.168.188.131',23000) )
clisock.send("hello world\n")
print clisock.recv(100)
clisock.close()

# based off of this tutorial:
#http://www.binarytides.com/python-socket-programming-tutorial/

import socket
import time
import sys

# socket.SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print s

server = 'google.com'
port = 80
server_setup = (server, port)

server_ip = socket.gethostbyname(server)
print server_ip

request = "GET / HTTP/1.1\nHOST: " + server + "\n\n"

s.connect(server_setup)

#s.send(request.encode())    # python3
s.send(request)

result = s.recv(4096)

#print result

# buffering
while (len(result) > 0):
    print result
    result = s.recv(2)

s.close()
sys.exit(0)


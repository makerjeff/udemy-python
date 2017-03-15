import socket
import sys

host = ''
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))

except socket.error as e:
    print str(e)

s.listen(5)
print 'waiting for connection...'

connection, client_addr = s.accept()
print 'connected to: ' + client_addr[0] + ':' + str(client_addr[0])
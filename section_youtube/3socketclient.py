import binascii
import socket
import sys

# create tcp/ip connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.90.42.85', 12345)
sock.connect(server_address)

# data
data = 'Here lies a string of text that will be sent to the server.'

try:
    # send data
    print 'sending data: ' + binascii.hexlify(data)
    sock.sendall(binascii.hexlify(data))

finally:
    print 'closing socket'
    sock.close()

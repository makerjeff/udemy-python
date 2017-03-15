# MORE ABOUT STRUCTS
# https://docs.python.org/2/library/struct.html

import binascii
import socket
import struct
import sys

my_string = 'this is my string of data. get the length from len()'

#create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.90.42.85', 12345)
sock.bind(server_address)
sock.listen(1)

# unpacker = struct.Struct('I 2s f')
unpacker = struct.Struct('s')

while True:
    print >> sys.stderr, '\n waiting for a connection...'

    connection, client_address = sock.accept()

    try:
        data = connection.recv(unpacker.size)
        print >>sys.stderr, 'recieved "%s"' % binascii.hexlify(data)

        unpacked_data = unpacker.unpack(data)
        print >>sys.stderr, 'unpacked: ', unpacked_data

    finally:
        connection.close()

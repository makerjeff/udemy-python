# learn more about binascii here:
# https://docs.python.org/2/library/binascii.html

# go through this sentdex tutorial:
# https://www.youtube.com/watch?v=wzrGwor2veQ

import binascii
import socket
import sys

file = open('../section_17/images/jeff.jpg', 'rb')

# create server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.90.42.85', 12345)
sock.bind(server_address)
sock.listen(5)

#

while True:
    print >>sys.stderr, '\n waiting for a connection...'

    # grab data sent from client
    connection, client_address = sock.accept()

    try:
        data = connection.recv(1024)

        # write data back to client.
        print >>sys.stderr, 'received "%s"' % data
        print 'converting back to string: '
        print binascii.unhexlify(data)

    finally:
        connection.close()




# learn more about binascii here:
# https://docs.python.org/2/library/binascii.html

# potentially use this too: cStringIO (faster version of StringIO)
# https://docs.python.org/2/library/stringio.html

# go through this sentdex tutorial:
# https://www.youtube.com/watch?v=wzrGwor2veQ

# TODO: THIS WORKS, sending and receiving arrays over sockets
# http://stackoverflow.com/questions/7107075/sending-and-receiving-arrays-via-sockets

import binascii
import socket
import sys
import cv2
import pickle


# create server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.90.42.85', 12345)
sock.bind(server_address)
sock.listen(5)

#

def send_image_file(file):
    img = cv2.imread(file)
    data = pickle.dumps(img)
    return data


while True:
    print >>sys.stderr, '\n waiting for a connection...'

    # grab data sent from client
    connection, client_address = sock.accept()

    try:
        # data = connection.recv(1024)
        #
        # # write data back to client.
        # print >>sys.stderr, 'received "%s"' % data
        # print 'converting back to string: '
        # print binascii.unhexlify(data)

        print 'sending data...'
        connection.send(send_image_file('../section_17/images/jeff.jpg'))


    finally:
        connection.close()




import binascii
import socket
import sys
import pickle
import cv2

# create tcp/ip connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.90.42.85', 12345)
sock.connect(server_address)

# data
data = 'Here lies a string of text that will be sent to the server.'

def show_file(data):
    datum = data
    imgarr = pickle.loads(datum)
    return imgarr

    #TODO: use CV2.imshow loop to display image just downloaded

try:
    # # send data
    # print 'sending data: ' + binascii.hexlify(data)
    # sock.sendall(binascii.hexlify(data))
    show_file(sock.recv(2048))



finally:
    # print 'closing socket'
    sock.close()

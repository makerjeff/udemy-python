from PIL import Image
import socket
import cv2
import numpy as np
import matplotlib.pyplot as plt

def send_image_file(file):
    img = Image.open(file)
    iar = np.asarray(img)

    return iar  # start with the binary object first... then if this doesn't work, send the image array.


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.90.42.85'
port = 12345
s.bind((host, port))

s.listen(5)
print 'listening on ' + host + ' on port ' + str(port)

while True:
    c, addr = s.accept()
    print 'Got connection from ', addr
    c.send(send_image_file('../section_17/images/jeff.jpg'))
    print 'sending image data...'
    c.close()
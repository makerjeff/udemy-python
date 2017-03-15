from PIL import Image
import socket
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# FUNCTIONS =====================
# ===============================
def save_file_from_server(filename, data):
    """Save data straight to a file."""
    with open(filename, 'wb') as file:
        file.write(data)

def show_file(data):
    iar = data
    plt.imshow(iar)
    print iar
    plt.show()





# ===============================
# SETUP =========================
s = socket.socket()
host = '10.90.42.85'
port = 12345

s.connect((host, port))
#print s.recv(1024)
#save_file_from_server('../saved_file.png', s.recv(1024))
show_file(float(s.recv(2048)))

s.close()
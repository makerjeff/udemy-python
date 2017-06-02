# =============
# TCP - CLIENT
# =============
#connect((hostname, port))
#recv(buffer)
#send(bytes)
#close()

import socket

def Main():

    # --- setup ---
    hostname = '127.0.0.1'  #server to connect to
    port = 5000             #port of server

    s = socket.socket()

    # --- connect ---
    s.connect((hostname, port))

    # --- ask user for input ---
    message = raw_input('-> ')


    # --- main loop ---
    while message != 'q':
        s.send(message)

        data = s.recv(1024)
        print 'Received from server: ' + str(data)

        message = raw_input('-> ')

    # --- exit main loop, close socket connection ---

    s.close()

if __name__ == '__main__':
    Main()


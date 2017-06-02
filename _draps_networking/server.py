#=============
#TCP - SERVER
#=============
#socket(socket_family, socket_type)
#bind ((hostname, port));
#listen()
#accept()

import socket

def Main():

    # --- SETUP ---
    hostname = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((hostname, port))

    # --- start listening ---
    s.listen(1)
    print 'server started listening...'


    # --- grab returned connection and address ---
    c, addr = s.accept()

    print 'Connection from: ' + str(addr)

    # --- main loop ---
    while True:
        data = c.recv(1024)

        if not data:
            break

        print 'from connected user: ' + str(data)

        data = str(data).upper()

        print 'sending: ' + str(data)

        c.send(data)

    # --- exiting the main loop, close connection.
    c.close()

if __name__ == '__main__':
    Main()


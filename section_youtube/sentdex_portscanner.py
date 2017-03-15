import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #TCP
server = '10.90.42.85'

def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False

for x in range(1,26):
    if pscan(x):
        print 'Port ' + str(x) + ' is open.'
    else:
        print 'Port ' + str(x) + ' is closed.'
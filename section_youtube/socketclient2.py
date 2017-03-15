import binascii
import socket
import struct
import sys

#create tcp/ip connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.90.42.85', 12345)
sock.connect(server_address)

# values = (1, 'ab', 2.7)
values = 'some ascii data message'

# packer = struct.Struct('I 2s f')
packer = struct.Struct('s')

packed_data = packer.pack(*values)

try:
    # send data
    print >>sys.stderr, 'sending "%s"' % binascii.hexlify(packed_data), values
    sock.sendall(packed_data)

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
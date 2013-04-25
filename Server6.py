import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.bind(("", 8081))

while True:
    data, addr = s.recvfrom(1024)
    print "Received: ", data, "from: ", addr


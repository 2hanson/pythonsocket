import socket
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
port = 8081
host = "::1"
while True:
        msg = raw_input()
        s.sendto(msg, (host, port))

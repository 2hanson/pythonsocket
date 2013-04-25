import socket
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
fb = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
port = 5060
host = "2001:cc0:2026:e00:0:0:0:707"
fb.bind(('', 47769))
cnt = input()
while cnt>0:
        usr = "<sip:cngi32009707c@domain3.com>"
        msg = "REGISTER sip:[2001:cc0:2026:e00::707]:5060 SIP/2.0\nCall-ID: 31c4bc01fd23721310c94ecff1ea0b9b@2001:cc0:2026:e00:bdef:4957:1e58:eecf\nCSeq: 1 REGISTER\nFrom: "+ usr +";tag=2952\nTo: "+ usr +"\nVia: SIP/2.0/UDP [2001:cc0:2026:e00:bdef:4957:1e58:eecf]:47769;branch=z9hG4bK9d925f6e592528f91c331504dfdc9e66\nMax-Forwards: 2\nContact: <sip:cngi32009707c@[2001:cc0:2026:e00:bdef:4957:1e58:eecf]:47769;transport=udp;user=UA>;expires=3600\nExpires: 3600\nContent-Length: 0\n"
        s.sendto(msg, (host, port))
        print fb.recvfrom(1024)
        cnt -= 1


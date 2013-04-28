import time
import random
import socket
import string
import sys

s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
fb = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
port = 5060
host = "2001:cc0:2026:e00:0:0:0:707"
fb.bind(('', 47769))
cnt = input()
tmp = cnt
while cnt>0:
        random.seed(cnt)
        uid = cnt % 100;
        uid = 20000 + uid;
        list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        items = [t for t in range(0, 32)]
        for index in range(32):
            tid = random.randint(0, 15)
            items[index] = list[tid]
        random.shuffle(items)
        callid = string.join(random.sample(items, 32)).replace(" ", "");        
        #fellow 3 line is comments 
        #tmpstr = "32009707c";
        #usr = "<sip:cngi" + tmpstr + "@domain3.com>"
        #usr = "<sip:cngi" + str(uid) + "@domain3.com>"
        print "callid = " + callid        
        msg = "REGISTER sip:[2001:cc0:2026:e00::707]:5060 SIP/2.0\nCall-ID: "+ callid +"@2001:cc0:2026:e00:bdef:4957:1e58:eecf\nCSeq: 1 REGISTER\nFrom: <sip:cngi"+ str(uid) +"@domain3.com>;tag=2952\nTo: <sip:cngi"+ str(uid) +"@domain3.com>\nVia: SIP/2.0/UDP [2001:cc0:2026:e00:bdef:4957:1e58:eecf]:47769;branch=z9hG4bK9d925f6e592528f91c331504dfdc9e66\nMax-Forwards: 2\nContact: <sip:cngi" + str(uid) + "@[2001:cc0:2026:e00:bdef:4957:1e58:eecf]:47769;transport=udp;user=UA>;expires=3600\nExpires: 3600\nContent-Length: 0\n"
        s.sendto(msg, (host, port))
        fbmsg, addr = fb.recvfrom(1024)
        print 'message from server: %d: %s' % (tmp-cnt+1, fbmsg[0:97])
        cnt -= 1
        time.sleep(1)


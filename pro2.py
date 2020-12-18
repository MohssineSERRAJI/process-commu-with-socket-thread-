import socket
import threading
import random
import time
from queue import Queue 
from threading import Thread

UDP_IP = "127.0.0.1"
UDP_PORT_TO_RECIVE = 5005
UDP_PORT_TO_SEND = 5006

tempurature = [random.randint(0, 50)]

end = random.randint(5, 10)

def send_thread(in_q):
    print("From Client proc 2")
    global end
    MESSAGE = str(in_q.get()[0]).encode()
    print(MESSAGE)
    # create an INET, STREAMing socket
    while True:
        sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
        time.sleep(end)
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_TO_SEND))
        print("Send : "+MESSAGE.decode("utf-8") )
        MESSAGE = str(in_q.get()[0]).encode()



def recive_thread(out_q):
    print("From server pro 2")
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT_TO_RECIVE))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)
        out_q.put(data)


q = Queue() 
q.put(tempurature)
x = threading.Thread(target=send_thread, args=(q, ))
y = threading.Thread(target=recive_thread, args=(q, ))
x.start()
y.start()

import socket
import threading
import random
import time


UDP_IP = "127.0.0.1"

UDP_PORT_TO_RECIVE = 5006 #same to UDP_PORT of the last proc
UDP_PORT_TO_SEND = 5005 #same like pro2

tempurature = random.randint(0, 50)

end = random.randint(5, 10)

def send_thread(var):
    print("From Client proc 1")
    global end
    MESSAGE = str(var).encode()
    # create an INET, STREAMing socket
    while True:
        sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
        time.sleep(end)
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_TO_SEND))
        print("Send : "+MESSAGE.decode("utf-8") )
        MESSAGE = str(var).encode()



def recive_thread(var):
    print("From server pro 1")
    global tempurature
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT_TO_RECIVE))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)
        var = data


x = threading.Thread(target=send_thread, args=(tempurature, ))
y = threading.Thread(target=recive_thread, args=(tempurature, ))
x.start()
y.start()
x.join()
y.join()


import schedule
import time
def send_receive():
    #ACCEPT FROM C
    import socket
    import random
    #ACCEPT FROM B
    msg='hello  UDP server'
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(msg.encode('utf-8'),('127.0.0.1', 12347))
    data,addr=client_socket .recvfrom(4094)
    print('addr client'+str(addr))
    print('I am D i received this temp : '+str(data))
    TEMP=str(data)
    client_socket.close()

    #SENDING D-A

    sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 12345))

    while True:
        data,addr=sock.recvfrom(4096)
        n = random.randint(0,100)
        message='hello i am D with the number'+str(n)
        print('addr server'+str(addr))
        print('i  am D i will send this temp :'+str(data))
        sock.sendto(str(TEMP).encode(),addr)

#Send and receive temp every 100 MS 
schedule.every(0.1).seconds.do(send_receive)

while 1:
    schedule.run_pending()
    time.sleep(1)

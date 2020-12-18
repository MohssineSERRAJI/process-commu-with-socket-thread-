import schedule
import time


def send_receive():
    #SENDING A-B
    import socket
    import random
    sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 12345))

    while True:
        data,addr=sock.recvfrom(4096)
        print(str(data))
        message='hello i am A'
        n = random.randint(0,100)
        TEMP = random.randint(0,50)
        msg=str(n)+str(TEMP)
        print(str(message))
        print('i will send this temp : '+str(TEMP))

        sock.sendto(str(TEMP).encode(),addr)

    #ACCEPT FROM D
    import socket
    import random

    client_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg='hello  UDP server'

    client_socket.sendto(msg.encode('utf-8'),('127.0.0.1', 12347))
    data,addr=client_socket .recvfrom(4094)
    print('addr client'+str(addr))
    print('I am D i received this temp : '+str(data))
    TEMP=str(data)
    client_socket.close()

#Send and receive temp every 100 MS 
schedule.every(0.1).seconds.do(send_receive)

while 1:
    schedule.run_pending()
    time.sleep(1)

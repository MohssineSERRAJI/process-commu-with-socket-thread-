

import schedule
import time

def send_receive():
    #ACCEPT FROM A
    import socket
    import random
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg='hello  UDP server'

    client_socket.sendto(msg.encode('utf-8'),('127.0.0.1', 12345))
    data,addr=client_socket .recvfrom(4096)
    print('addr client'+str(addr))
    print('i am  B i received :'+str(data))
    print(str(data))
    TEMP=str(data)
    client_socket.close()


    #SENDING B-C

    sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 12346))

    while True:
        data,addr=sock.recvfrom(4095)
        print(str(data))
        n = random.randint(0,100)
        message='hello i am B with the number'+str(n)
        msg=str(n)+str(TEMP)
        print('addr server'+str(addr))
        print('msg'+str(msg))
        print('i will send this temp :'+str(data))
        sock.sendto(str(TEMP).encode(),addr)


#Send and receive temp every 100 MS 
schedule.every(0.1).seconds.do(send_receive)

while 1:
    schedule.run_pending()
    time.sleep(1)
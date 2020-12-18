
import schedule
import time
def send_receive():
    import socket
    import random
    #ACCEPT FROM B
    msg='hello  UDP server'
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(msg.encode('utf-8'),('127.0.0.1', 12346))
    data,addr=client_socket .recvfrom(4095)
    print('addr client'+str(addr))
    print('Hi i am C and i receiveid the temp : '+str(data))
    TEMP=str(data)
    client_socket.close()

    #SENDING C-D

    sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 12347))

    while True:
        data,addr=sock.recvfrom(4094)
        print(str(data))
        n = random.randint(0,100)
        message='hello i am C with the number'+str(n)
        print('addr server'+str(addr))
        print('i am C will send this temp :'+str(data))
        sock.sendto(str(TEMP).encode(),addr)

#Send and receive temp every 100 MS 
schedule.every(0.1).seconds.do(send_receive)

while 1:
    schedule.run_pending()
    time.sleep(1)

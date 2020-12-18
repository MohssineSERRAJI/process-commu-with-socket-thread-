import socket
import threading
import random

server_port = 1022
client_port = 1021

tempurature = random.randint(0, 50)

end = random.randint(10000, 20000)

def send_thread(end, tempurature):
    print("from client")
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    #connect to resever
    s.connect(("localhost",client_port))
    print("from client 2 connection done")
    while True:
        if end == 0:
            break
        end -= 1
    st='connection done'
    byt=st.encode()
    s.send(byt)



def recive_thread():
    print("from server")
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    #connect to resever
    s.bind(("localhost", server_port))
    #queue of 5 connection
    s.listen(5)
    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = s.accept()
        print("socket accepted"+str(clientsocket))
        data = s.recv(1024)
        if not data: break
        print(f"tempuratue from 1."+data)

"""
x = threading.Thread(target=send_thread, args= (end, tempurature))
y = threading.Thread(target=recive_thread)
x.start()
y.start()
"""

recive_thread()
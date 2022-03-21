import socket
import threading

from pymysql import NULL

serverip = 'localhost'
port = 3000

clist = {}

def client_msg(client,addr):
    data = NULL
    while True:
        try:
            data  = (client.recv(4096).decode('utf-8'))
        except:
            clist.pop(client)
            break
        if (not data) or data == 'exit':
            #print('not data')
            clist.pop(client)
            break
        else:
            print("mas from client{}>>>{}".format(addr,data))
            client.send('login'.format(data).encode('utf-8'))
            

        
    client.close()

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #Set Socket Option ให้ Socket ใช้ Port เดียวกัน
server.bind((serverip,port))
server.listen(5)

print('server on')

while True:
    client, addr = server.accept()
    clist[client] = [addr,0,NULL]
    client.send('1. Login\n2. Register\n3. Exit'.encode('utf-8'))
    print(client)
    print('กำลังออนไลน์',len(clist),'คน')
    task = threading.Thread(target=client_msg,args=(client,addr))
    task.start()

#klayut 633020032-4 
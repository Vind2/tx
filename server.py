__author__ = 'Vincent'

import tx, socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(('localhost',7777))

sock.listen(10)

while True:
    client, addr = sock.accept()

    rcdString = client.recv(1024)

    serverAction = tx.ServerAction(rcdString)

    serverAction.transact()

    client.send(serverAction.returnMsg)

    client.close()

#loop
    #recieve
#rcdString = raw_input("INPUT STRING: ")
#serverAction = tx.ServerAction(rcdString)
#serverAction.transact()




        #return to client - serverAction.returnMsg

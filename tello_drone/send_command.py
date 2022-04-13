import socket

localIP = "127.0.0.1"
localPort  = 20001

#Create a socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#drone address
tello_address = ('192.168.10.1', 8889)

#Bind to address and ip
UDPServerSocket.bind((localIP,localPort))

#Listen for incoming datagrams
while True:
    try:
        #Input command
        #command: enter SDK mode
        msg = input('')
        if not msg:
            break
        if 'end' in msg:
            UDPServerSocket.close()
            break
        msg = msg.encode()
        print(msg.decode())
        #Send a message to client
        UDPServerSocket.sendto(msg, tello_address)
    except Exception as err:
        print(err)
        UDPServerSocket.close()
        break

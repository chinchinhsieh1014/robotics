import socket

localIP = "0.0.0.0"
localPort  = 8890
bufferSize = 1024

#Create a socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#drone address
tello_address = ('192.168.10.1', 8889)

#Bind to address and ip
UDPServerSocket.bind((localIP,localPort))

#Listen for incoming datagrams
while True:
    try:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        #Message from Client
        message = bytesAddressPair[0]
        #Client IP Address
        address = bytesAddressPair[1]
        print(message.decode())
    except Exception as err:
        print(err)
        UDPServerSocket.close()
        break

UDPServerSocket.close()

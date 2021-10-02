from socket import *
import sys
#open a socket
serverSocket = socket(AF_INET,SOCK_STREAM)

port = 6789
#bind the socket to a server port
serverSocket.bind(('',port))
#Listen on the socket
serverSocket.listen()
#Fill in end

#loop forever
while True:
    #print message
    print("The server is ready to receive...")
    #accept incomming request
    connectionSocket, add = serverSocket.accept()

    try:
        #receve and decode
        message = connectionSocket.recv(1024).decode()
        #extract file path
        filename = message.split()[1]

        #open file
        f = open(filename[1:])
        #read data from file
        outputdata = f.read()

        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        #Fill in end

        #Send the content of the requested file to the client
        #send HTTP response header line
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        #send http content data
        connectionSocket.send(message.encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        #close client connection socket
        connectionSocket.close()
        #server prints OK
        print('HTTP 200 OK')

    except IOError:
        #Send response message for file not found
        #send http 404
        connectionSocket.send('HTTP/1.1 404 NOT FOUND\r\n'.encode())
        #server print 404
        print("404 NOT FOUND")
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
    #close server socket
    serverSocket.close()
    #exit
    sys.exit()
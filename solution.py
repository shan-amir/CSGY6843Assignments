# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(('0.0.0.0', port))

    serverSocket.listen(1)

    while True:
        # Establish the connection

        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]

            # opens the client requested file.
            f = open(filename[1:])
            contents = f.read()
            f.close()

            # Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
            validresponse = 'HTTP/1.1 200 OK\n\n' + contents
            connectionSocket.sendall(validresponse.encode())
            # for i in f:  # for line in file
                # connectionSocket.send(i.encode())
            connectionSocket.close()  # closing the connection socket

        except Exception as e:
            connectionSocket.send(b"HTTP/1.1 404 NOT FOUND")
            connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)

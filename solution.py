# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))

    serverSocket.listen(1)

    while True:
        # Establish the connection

        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]

            # opens the client requested file.
            f = open(filename[1:], "r")

            outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"

            # Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
            validresponse = b"HTTP/1.1 200 OK\r\n Connection: close\r\n"
            validresponse += outputdata
            connectionSocket.send(validresponse)

            for i in f:  # for line in file
                connectionSocket.send(f.readlines())
            connectionSocket.close()  # closing the connection socket

        except Exception as e:
            connectionSocket.send(b"HTTP/1.1 404 Not Found")
            break

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)

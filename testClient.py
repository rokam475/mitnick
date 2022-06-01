import socket
defaultSocketDomain = socket.AF_INET
defaultSocketType = socket.SOCK_STREAM
clientSocket = socket.socket(defaultSocketDomain, defaultSocketType)
myIp = socket.gethostname()
serverPort = 5000

clientSocket.connect((myIp, serverPort))
clientSocket.sendall(b"Hello world")
data = clientSocket.recv(1024)
print(data)

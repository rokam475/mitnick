from mimetypes import init
import socket
import threading

defaultSocketDomain = socket.AF_INET
defaultSocketType = socket.SOCK_STREAM
serverSocket = socket.socket(defaultSocketDomain, defaultSocketType)
hostIp = socket.gethostname()
port = 5000
maxConnections = 5
packetSize = 1024

# serverSocket.bind((hostIp, port))
# serverSocket.listen(maxConnections)
# while True:
#     client, addr = serverSocket.accept()
#     print("accepting")
#     while True:
#         data = client.recv(packetSize)
#         if not data:
#             break
#         print(data)
#         client.sendall(data)

class socketListener(threading.Thread):
    def __init__(self) -> None:
        super().__init__()
        self.setDaemon(True)   
        serverSocket.bind((hostIp, port))
        serverSocket.listen(maxConnections)

        
    def run(self):
        while True:
            client, addr = serverSocket.accept()
            print("accepting")
            while True:
                data = client.recv(packetSize)
                if not data:
                    break
                print(data)
                client.sendall(data)     

server = socketListener()
server.start()
while True:
    pass

import socket
import pickle
defaultPacketSize = 32768
defaultPort = 5555
defaultSocketDomain = socket.AF_INET
defaultSocketType = socket.SOCK_STREAM
ackID = 1
resetID = 0
proto=5

class Osiris:
    def __init__(self, myIp=socket.gethostname(), packetSize=defaultPacketSize, socketDomain=defaultSocketDomain, socketType=defaultSocketType):
        self.socket = socket.socket(socketDomain, socketType)

        self.myIp = myIp
        self.port = port
        self.addr = (self.server, self.port)
        self.packetSize = packetSize

    def handshake(self):
        self.socket.bind((, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


        def send(self, connection, payload):
        serialized = self.encrypt(payload)
        syn = len(serialized)
 

        connection.send(self.encrypt(syn)) # sed all packets as seralized objects
        ack = connection.recv(self.packetSize)
        if ack and self.decrypt(ack) == ackID:
            connection.send(serialized)
            return 1
        elif ack:
            print("packet too big")
        else:
            print("missing ack")
        return 0
import socket
import pickle


defaultPacketSize = 32768
defaultPort = 5555
defaultSocketDomain = socket.AF_INET
defaultSocketType = socket.SOCK_STREAM
ackID = 1
resetID = 0
proto=5

class Network():
    def __init__(self, myIp=socket.gethostname(), packetSize=defaultPacketSize, socketDomain=defaultSocketDomain, socketType=defaultSocketType):
        self.socket = socket.socket(socketDomain, socketType) # init socket
        self.myIp = myIp            # current IP
        self.packetSize = packetSize    # max packet size

    def send(self, data, connection): # send data with pickle
        connection.send(pickle.loads(data, protocol=proto)) # send pickled data to connection

    def recv(self, connection): # recive pickled data
        data = connection.recv(self.packetSize) # get the data
        return pickle.dumps(data, protocol=proto) # return unpickled data
from mimetypes import init
from Network import Network
import threading

defaultMaxConnections = 5

# class serverThread(self):
#     def __init__(self) -> None:
#         super().__init__()


class Server(Network):
    def __init__(self, maxConnections = defaultMaxConnections):
        super().__init__()
        self.connectionIds = [False] * maxConnections # truth array of available connections
        self.connections = {} # dict of connections
        self.threads = {} # dict of threads
        self.running = False # server status

    def serverThread(self, id, connection, address): # server functionality to be implemented
        self.send('No server side implementation', connection) # if not implemented send error to client
        while self.connectionIds[id]:   # while connection is open
            continue

    def closeConnection(self, connectionId): # close connection
        self.connections[connectionId].close() # close connection
        del self.connections[connectionId] # remove connection info from dict
        self.connectionIds[connectionId] = False

    def startConnection(self, connection, address):
        for curId in range(len(self.connectionIds)):
            if not self.connectionIds[curId]:
                self.connectionIds[curId] = True
                threading.Thread(target=self.serverThread, args=(curId, connection, address))
                self.connections[curId] = connection
            else:
                print("no open connections")
    
    
    def startServer(self, port, maxConnections=defaultMaxConnections):
        with self.socket as s:
            s.bind((self.myIp, port))
            s.listen(maxConnections)

            running = True
            while running:
                connection, address = self.socket.accept()
                self.startConnection(connection, address)
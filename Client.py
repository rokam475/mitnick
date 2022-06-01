from Network import Network
class Client(Network):
    def __init_subclass__(self) -> None:
        super().__init__()
        self.connection = None

    def connect(self, targetIp, targetPort):
        self.connection = self.socket.connect((targetIp, targetPort))
        print(self.connection)
    

        
    
    
    
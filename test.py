from Server import Server
from Client import Client

serverPort = 500

osiris = Server()
mitnick = Client()

print("launch")
osiris.startServer(serverPort)
# mitnick.connection(osiris.myIp, serverPort)
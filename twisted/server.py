from unicodedata import name
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, connectionDone
from twisted.internet.protocol import ServerFactory as servFactory
from twisted.internet.endpoints import TCP4ServerEndpoint

class Server(Protocol):
    def __init__(self, users):
        self.users = users
        self.name = ""

    def connectionMade(self):
        print('new conncetion')
        self.transport.write("Hello from server\n".encode('utf-8'))
        self.transport.write("Write Your name: ".encode('utf-8'))
    
    def addUser(self, nameRecived):         
        if nameRecived not in self.users:
            self.users[self] = nameRecived
            self.name = nameRecived
        else:
            self.transport.write("Wrong username, try another one".encode("utf-8"))
    
    def dataReceived(self, data: bytes):
        data = data.decode("utf-8")

        if not self.name:    
            self.addUser(data)
            return

        for protocol in self.users.keys():
            if(protocol != self):
                protocol.transport.write(f"{self.name}: {data}".encode("utf-8") )
    
    def connectionLost(self, reason = connectionDone):
        del self.users[self]

class ServerFactory(servFactory):
    def __init__(self):
        self.users = {}

    def buildProtocol(self, addr):
        return Server(self.users)
    
if __name__ == '__main__':
    endpoint = TCP4ServerEndpoint(reactor, 2000)
    endpoint.listen(ServerFactory())
    reactor.run()
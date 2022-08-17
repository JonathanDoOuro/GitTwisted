from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ServerFactory as servFactory
from twisted.internet.endpoints import TCP4ServerEndpoint
class Server(Protocol):
    def __init__(self, users):
        self.users = users

    def connectionMade(self):
        print('new conncetion')
        self.users.append(self)
        self.transport.write("Hello from server\n".encode('utf-8'))
    
    def dataReceived(self, data: bytes):
        for user in self.users:
            user.transport.write(data)

class ServerFactory(servFactory):
    def __init__(self):
        self.users = []

    def buildProtocol(self, addr):
        return Server(self.users)
    
if __name__ == '__main__':
    endpoint = TCP4ServerEndpoint(reactor, 2000)
    endpoint.listen(ServerFactory())
    reactor.run()
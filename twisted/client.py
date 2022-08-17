from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ClientFactory as CliFactory
from twisted.internet.endpoints import TCP4ClientEndpoint

class Client(Protocol):
    def dataReceived(self, data):
        data = data.decode('utf-8')
        print(data)
        self.transport.write(input(":::").encode('utf-8'))

class ClientFactory(CliFactory):
    def buildprotocol(self, addr):
        return Client()


if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 2000)
    endpoint.connect(ClientFactory())
    reactor.run()

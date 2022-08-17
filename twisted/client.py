from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ReconnectingClientFactory as CliFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from sys import stdout

class Client(Protocol):
    def __init(self):
        reactor.callInThread()

    def dataReceived(self, data):
        data = data.decode('utf-8')
        stdout.write(data)

    def send_data(self):
        while True:
            self.transport.write(input().encode('utf-8'))

class ClientFactory(CliFactory):
    def buildprotocol(self, addr):
        return Client()

    def clientConnectionFailed(self, connector, reason):
        print(reason)
        CliFactory.clientConnectionFailed(self, connector, reason)

    def clientConnectionLost(self, connector, reason):
        print(reason)
        CliFactory.clientConnectionLost(self, connector, reason)

if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 2000)
    endpoint.connect(ClientFactory())
    reactor.run()

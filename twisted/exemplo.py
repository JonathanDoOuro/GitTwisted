from twisted.application import service, strports
from twisted.internet import protocol, reactor, defer
from twisted.protocols import basic


#basic.LineReceiver - (A protocol that receives lines and/or raw data, depending on mode.)
class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, user):
        # Deferred - the program can perform other operations in the meantime, 
        # and waits for some signal that data is ready to be processed 
        # before returning to that process.
        d = self.factory.getUser(user)

        def onError(err):
            return b'Internal error in server'
        d.addErrback(onError)

        def writeResponse(message):
            self.transport.write(message + b'\r\n')
            self.transport.loseConnection()
        d.addCallback(writeResponse)

class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol

    def __init__(self, users):
        self.users = users

    def getUser(self, user):
        return defer.succeed(self.users.get(user, b"No such user"))

        
#one end of a connection.
#There are different endpoints for clients and servers.
#tells Twisted to look for a TCP endpoint, and pass it the port 1079.
#fingerEndpoint = endpoints.serverFromString(reactor, "tcp:1079")

#causes Twisted to start listening on port 1079.
#for each request, the reactor calls the factory’s buildProtocol method
application = service.Application('finger', uid=1, gid=1)
factory = FingerFactory({b'moshez': b'Happy and well'})
strports.service("tcp:79", factory, reactor=reactor).setServiceParent(
    service.IServiceCollection(application))
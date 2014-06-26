# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


"""
A client that does random things, for testing.
"""

from twisted.internet import reactor, protocol
from randomplayer import RandomPlayer

"""
TODO:
- should also ask for games list...
"""

# a client protocol
class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""

    def __init__(self):
        self.player = RandomPlayer()
    
    def connectionMade(self):
        print 'client connected'
        init_string = self.player.get_init_string()
        self.transport.write(init_string)
    
    def dataReceived(self, data):
        #print "Server said:\n", data
        if data.strip().split('\n')[0] == 'board':
            # get the board
            self.player.receive_board(data)
            # make a move
            self.transport.write(self.player.move())
        elif 'Game Over!' in data:
            # wow plz fix this hackiness
            self.transport.loseConnection()
    
    def connectionLost(self, reason):
        print "connection lost"

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        #reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        #reactor.stop()


# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()
    for i in range(400):
        reactor.connectTCP("localhost", 8000, f)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()

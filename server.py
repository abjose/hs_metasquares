# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


"""
TODO:
- should prepend all messages with something - even warning/success messages?
  like 'message'
- handle messages better if prepending them with stuff, can just send lots!
  like every one that occurs
  or at least print them out server-side

Accepted patterns:
'init' player_name game_name rows cols num_players score_limit (make/enter game)
'games' (list of games waiting for players)
'move' row column (make a move)

Data sent to client:
'board' rows cols \n r c player \n r c player \n ... (sparse board rep)
'games' game1 \n game2 \n ...
various messages (not beginning with 'board')
"""

from twisted.internet import reactor, protocol
from game_master import GameMaster

class Echo(protocol.Protocol):

    def connectionMade(self):
        print "Got new client!"
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        print "Lost a client!"
        self.factory.clients.remove(self)
    
    def dataReceived(self, data):
        # try to handle data
        handler = {'init'  : self.handle_data,
                   'games' : self.handle_game_list,
                   'move'  : self.handle_move,}
        data = data.strip().split()
        try:
            handler[data[0]](data)
        except Exception:
            # probably got incorrectly formatted input
            self.transport.write('Bad data format!')

    def send_board(self, game):
        player = self.factory.GM.get_next_player(game)
        board_state = repr(self.factory.games[game].board)
        self.factory.p2c[(player,game)].transport.write('board\n'+board_state)

    def handle_move(self, data):
        try:
            _, r, c = data
        except Exception:
            print 'Got poorly formatted move...'
            self.transport.write("Move is badly formatted!")
        else:
            if self not in self.factory.p2c.values():
                print "Not in a game!"
                self.transport.write("Initialize a game before moving!")
            else:
                player, game = {v:k for k,v in self.factory.p2c.items()}[self]
                success, msg = self.factory.GM.move(game, int(r),int(c), player)
                # send board state to next player
                # this seems like a hack
                # but better than giving gamemaster an instance of factory?
                self.send_board(game)

    def handle_game_list(self, data):
        waiting_games = [g for g in self.factory.GM.games
                          if not self.factory.GM.games[g].is_game_started()]
        self.transport.write("games\n" + "\n".join(waiting_games))

    def handle_init(self, data):
        try:
            p_name, game_name, r, c, num_players, score_limit = data[1:]
        except Exception:
            print 'User passed in bad data: ' + data
            self.transport.write('Bad data format!')
        else:
            # try to add game and player
            self.factory.GM.add_game(game_name, int(r), int(c),
                                     int(num_players), int(score_limit))
            success, msg = self.factory.GM.add_player(p_name, game_name)
            if success:
                self.factory.p2c[(p_name, game_name)] = self
                # see if game should start
                if self.factory.GM.games[game_name].is_started():
                    # must be last player if game just started, so send board
                    self.send_board(game_name)
            self.transport.write(msg)

def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    factory.clients = []
    factory.GM = GameMaster()
    factory.p2c = {} # (player, game) -> client
    reactor.listenTCP(8000,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()

#!/usr/bin/env python

from game import Game

"""
Handle multiple games and players
Figure out where to send player commands
Should refactor so generally is player_name - game_name - other stuff
"""

class GameMaster(object):

    def __init__(self):
        self.games = {}

    def add_game(self, game_name, r, c, num_players, score_limit):
        # would prefer to put these checks into Game itself...
        if num_players <= 1:
            return False, "Game not made - num_players should be >= 2."
        if score_limit <= 0:
            return False, "Game not made - score_limit should be >= 1."
        if game_name in self.games:
            return False, "Game not made - there is already a game with that name."
        if not (r > 0 and c > 0):
            return False, "Game not made - the board size is invalid."
        self.games[str(game_name)] = Game(r, c, num_players, score_limit)
        return True, "Game '" + str(game_name) + "' successfully created."

    def add_player(self, player_name, game_name):
        if game_name not in self.games:
            return False,  "Player not added - that game doesn't exist."
        return self.games[game_name].add_player(player_name)

    def get_next_player(self, game_name):
        g = self.games[game_name]
        return g.players.keys()[g.player_index]
            
    def move(self, game_name, r, c, player_name):
        if game_name not in self.games:
            return False, "Move not made - that game doesn't exist."
        success, msg = self.games[game_name].move(r, c, player_name)
        if success:
            if not self.games[game_name].is_game_over():
                self.games[game_name].advance_turn()
            else:
                #msg += "\nGame Over!\n"+self.games[game_name].score_printout()
                msg = "Game Over!"#"\n" + self.games[game_name].score_printout()
                success = False
                #del self.games[game_name]
        return success, msg

    def remove_game(self, game):
        del self.games[game]
            
if __name__=='__main__':
    GM = GameMaster()
    print GM.add_game('test1', 10, 10, 2, 150)
    print GM.add_game('test2', 10, 10, 2, 150)
    print GM.add_game('test3', 10, 10, 2, 150)
    print GM.add_player('x', 'test1')
    print GM.add_player('x', 'test1')
    print GM.add_player(' ', 'test1')
    print GM.add_player('y', 'test1')
    print GM.add_player('z', 'test1')
    print GM.move('test1', 0, 0, 'x')
    print GM.move('test1', 0, 1, 'y')
    print GM.move('test1', 0, 0, 'z')
    print GM.move('test1', 0, 0, ' ')
    print GM.move('test2', 0, 0, 'x')
    #print GM.games['test1'].board

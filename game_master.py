#!/usr/bin/env python

from game import Game

"""
Handle multiple games and players
Figure out where to send player commands
"""

class GameMaster(object):

    def __init__(self):
        self.games = {}

    def add_game(self, game_name, r, c, num_players, score_limit):
        # would prefer to put these checks into Game itself...
        if num_players <= 0:
            return False, "Game not made - num_players should be >= 1."
        if score_limit <= 0:
            return False, "Game not made - score_limit should be >= 1."
        if game_name in self.games:
            return False, "Game not made - there is already a game with that name."
        self.games[str(game_name)] = Game(r, c, num_players, score_limit)
        return True, "Game '" + str(game_name) + "' successfully created."

    def add_player(self, game_name, player_name):
        if game_name not in self.games:
            return False,  "Player not added - that game doesn't exist."
        if player_name in [player for game in self.games.values() for player in game.players]:
            return False, "Player not added - that name already exists on the server."
        return self.games[game_name].add_player(player_name)
            
    def move(self, game_name, r, c, player_name):
        if game_name not in self.games:
            return False, "Move not made - that game doesn't exist."
        success, msg = self.games[game_name].move(r, c, player_name)
        if success:
            if not self.games[game_name].is_game_over():
                self.games[game_name].advance_turn()
            else:
                msg += "\nGame Over!\n" + self.games[game_name].score_printout()
                del self.games[game_name]
        return success, msg
            
if __name__=='__main__':
    GM = GameMaster()
    print GM.add_game('test1', 10, 10, 2, 150)
    print GM.add_game('test2', 10, 10, 2, 150)
    print GM.add_game('test3', 10, 10, 2, 150)
    print GM.add_player('test1', 'x')
    print GM.add_player('test1', 'x')
    print GM.add_player('test1', ' ')
    print GM.add_player('test1', 'y')
    print GM.add_player('test1', 'z')
    print GM.move('test1', 0, 0, 'x')
    print GM.move('test1', 0, 1, 'y')
    print GM.move('test1', 0, 0, 'z')
    print GM.move('test1', 0, 0, ' ')
    print GM.move('test2', 0, 0, 'x')
    #print GM.games['test1'].board

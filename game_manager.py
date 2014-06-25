#!/usr/bin/env python

from events_game import Game

"""
Handle multiple games and players
Figure out where to send player commands
"""

class MultiGame(object):

    def __init__(self):
        self.games = {}

    def add_game(self, game_name, r, c, num_players, score_limit):
        # would prefer to put these checks into Game itself...
        if num_players <= 0:
            return False, "Game not made - num players should be >= 1."
        if score_limit <= 0:
            return False, "Game not made - score limit should be >= 1."
        self.games[str(game_name)] = Game(r, c, num_players, score_limit)
        return True, "Game ''" + str(name) + "'' successfully created."

    def move(self, game_name, r, c, player_name):
        success, msg = self.games[game_name].move(r, c, player_name)
        if success:
            if not self.games[game_name].is_game_over():
                self.games[game_name].advance_turn()
            else:
                msg += "\nGame Over!\n" + self.games[game_name].score_printout()
        return success, msg
            

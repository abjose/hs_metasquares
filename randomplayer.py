#!/usr/bin/env python

# a random player, for testing the server

import random

"""
TODO:
- make a base class that does stuff like...generating init strings, etc.
"""

class RandomPlayer(object):

    def __init__(self):
        # come up with random stuff for making a game
        names = map(str, range(2))
        self.name = random.choice(names)
        self.game = 'game'+random.choice(names)
        self.rows, self.cols = random.randint(-1,10), random.randint(-1,10)
        #self.num_players = random.randint(-1,10)
        self.num_players = 2
        self.max_score = random.randint(-1,200)

    def get_init_string(self):
        # format:
        # 'init' player_name game_name rows cols num_players score_limit
        stats = ['init', self.name, self.game, self.rows, self.cols,
                 self.num_players, self.max_score]
        return ' '.join(map(str, stats))

    def move(self):
        # generate a move - might not be valid
        # format: 'move' row column
        print self.name, self.game, 'MOVING!'
        moves = [random.randint(-1,10), random.randint(-1,10)]
        return 'move ' +  ' '.join(map(str, moves))

    def receive_board(self, board):
        # this should go in base class
        print 'LENGTH OF BOARD DATA:', len(board.strip().split('\n'))

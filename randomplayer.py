#!/usr/bin/env python

# A random player, for testing the server.

import random
from player import Player

class RandomPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        # come up with random stuff for making a game
        names = map(str, range(10))
        self.board = None
        self.name = random.choice(names)
        self.game = 'game'+random.choice(names)
        self.rows, self.cols = random.randint(5,10), random.randint(5,10)
        self.num_players = random.randint(2,5)
        self.max_score = 150

    def move(self):
        # override Player's move with random movement
        moves = [random.randint(0,10), random.randint(0,10)]
        return 'move ' +  ' '.join(map(str, moves))

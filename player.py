#!/usr/bin/env python

# Base class for players. Reimplement 'move' to make your own player.

from grid import Grid

class Player(object):
    
    def __init__(self):
        self.board = None
        # boring defaults
        self.name = 'x'
        self.game = 'game'
        self.rows, self.cols = 10, 10
        self.num_players = 2
        self.max_score = 150
        
    def get_init_string(self):
        # format:
        # 'init' player_name game_name rows cols num_players score_limit
        stats = ['init', self.name, self.game, self.rows, self.cols,
                 self.num_players, self.max_score]
        return ' '.join(map(str, stats))

    def receive_board(self, board):
        self.board = Grid(load=board)
        print self.board
        
    def move(self):
        # format: 'move' row column
        return 'move 0 0'

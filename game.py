#!/usr/bin/env python

"""
Event-driven version of the game.
"""

from grid import Grid
from utils import Point, check_square, get_squares, get_square_score, get_scores
import pprint


"""
TODO:
- Just get rid of loop-y version? Or at least rewrite with these functions...
  Then switch this to just 'game' and switch that to game_loop or something
- Sure it's a good idea to return error messages?'
"""

class Game(object):

    def __init__(self, r, c, num_players, score_limit):
        # the board itself
        self.board = Grid(r, c)
        # game size and score limit
        self.num_players = num_players
        self.score_limit = score_limit
        # map from player names (i.e. 'pieces') to scores
        self.players = {}
        # keep track of current player
        self.player_index = 0
        # should precompute squares on init? or look for file and precompute 
        # if one isn't found

    def is_game_started(self):
        # should game start?
        return len(self.players) == self.num_players
        
    def is_game_over(self):
        # check if the game should end
        win = any([s >= self.score_limit for s in self.players.values()])
        no_moves = all([self.board[r][c] != self.board.default
                        for r in range(len(self.board))
                        for c in range(len(self.board[0]))])
        return not (win or no_moves)

    def score_printout(self):
        return "\n".join([p+": "+str(s)+ for p,s in self.players.items()])
        
    def move(self, r, c, player_name):
        # attempt to make a move
        if not (0 <= r < len(self.board) and 0 <= c < len(self.board[0])):
            return False, "Move not made - out of range."
        if self.board[r][c] != self.board.default:
            return False, "Move not made - that space is occupied."
        # otherwise, make move
        self.board[r][c] = player_name
        # and update scores
        squares = get_squares(self.board, (player_name, Point(r,c)))
        scores = get_scores(squares)
        players[player_name] += scores.get(player_name, 0)
        return True, "Move successful."

    def add_player(self, player_name):
        player_name = str(player_name)
        if player_name == self.board.default or player_name in self.players:
            return False, 'Please choose another name.'
        if len(self.players) == self.num_players:
            return False, 'This game is full.'
        self.players[player_name] = 0
        return True, 'Player added successfully'

    def advance_turn(self):
        self.player_index = (self.player_index+1) % self.num_players
                
if __name__=="__main__":
    # do some get_squares tests
    m = Game(10, 10)
    """
    P = [Point(0,0), Point(0,1), Point(1,0), Point(1,1)]
    print check_square(P)
    P = [Point(0,0), Point(0,2), Point(1,0), Point(1,1)]
    print check_square(P)
    P = [Point(0,0), Point(0,2), Point(2,0), Point(2,2)]
    print check_square(P)
    P = [Point(1,0), Point(0,1), Point(2,1), Point(1,2)] check_square(P)
    """

    """
    import random
    # try out filling lots of things
    for _ in range(30):
        m.board[random.randint(0,9)][random.randint(0,9)] = 'x'
        m.board[random.randint(0,9)][random.randint(0,9)] = 'o'
    print m.board
    squares = get_squares(m.board)
    pprint.pprint(squares)
    scores = get_scores(squares)
    pprint.pprint(scores)
    """
    m.run_game()


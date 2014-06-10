#!/usr/bin/env python
from grid import Grid
from utils import Point, check_square
from itertools import combinations
import pprint

"""
TODO:
- get score from area (just area of bounding box)
-----wait, really? that seems dumb
- allow players - ask how many players, use random characters, give
  scores at the end
- make AI? need to think about how best to interface with...

"""

class Metasquares(object):

    def __init__(self, r, c):
        self.board = Grid(r, c)
        # should precompute squares on init? or look for file and precompute 
        # if one isn't found

    def get_squares(self, ):
        # Return every found square in the grid
        # might be faster to pre-compute, but...ehhh.
        moves = self.board.get_moves()
        # split into different players
        players = dict()
        for pt, player in moves:
            players[player] = players.get(player, []) + [pt]
        # for each, get every combination of 4
        squares = dict()
        for player, plays in players.items():
            possibilities = list(combinations(plays, 4))
            for square in possibilities:
                if check_square(square):
                    squares[player] = squares.get(player, []) + [square]
        return squares

if __name__=="__main__":
    # do some get_squares tests
    m = Metasquares(10, 10)
    """
    P = [Point(0,0), Point(0,1), Point(1,0), Point(1,1)]
    print check_square(P)
    P = [Point(0,0), Point(0,2), Point(1,0), Point(1,1)]
    print check_square(P)
    P = [Point(0,0), Point(0,2), Point(2,0), Point(2,2)]
    print check_square(P)
    P = [Point(1,0), Point(0,1), Point(2,1), Point(1,2)]
    print check_square(P)
    """

    import random
    # try out filling lots of things
    for _ in range(30):
        m.board[random.randint(0,9)][random.randint(0,9)] = 'x'
    """
    m.board[1][0] = "x"
    m.board[0][1] = "x"
    m.board[2][1] = "x"
    m.board[1][2] = "x"

    m.board[0][0] = "x"
    m.board[0][1] = "x"
    m.board[1][1] = "x"
    m.board[1][1] = "x"

    m.board[3][3] = "o"
    m.board[5][4] = "o"
    m.board[4][6] = "o"
    m.board[2][5] = "o"
    """

    print m.board
    pprint.pprint(m.get_squares())


#!/usr/bin/env python

"""
 __  __ _____ _____  _    ____   ___  _   _   _    ____  _____ ____  
|  \/  | ____|_   _|/ \  / ___| / _ \| | | | / \  |  _ \| ____/ ___| 
| |\/| |  _|   | | / _ \ \___ \| | | | | | |/ _ \ | |_) |  _| \___ \ 
| |  | | |___  | |/ ___ \ ___) | |_| | |_| / ___ \|  _ <| |___ ___) |
|_|  |_|_____| |_/_/   \_\____/ \__\_\\___/_/   \_\_| \_\_____|____/ 
"""

from grid import Grid
from utils import Point, check_square, get_squares
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
    pprint.pprint(get_squares(m.board))


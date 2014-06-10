#!/usr/bin/env python

from grid import Grid
from utils import Point, check_square, get_squares, get_square_score, get_scores
import pprint

"""
TODO:
- make AI? need to think about how best to interface with...
"""

class Metasquares(object):

    def __init__(self, r, c):
        self.board = Grid(r, c)
        # should precompute squares on init? or look for file and precompute 
        # if one isn't found

    def run_game(self, num_players=2, score_limit=15):
        # run a game between num+players players
        assert(num_players > 0)
        players = dict([(str(r+1),0) for r in range(num_players)])
        player_index = 0
        print "Starting a game between", num_players, "players"
        print "Enter moves as a row and column separated by a space, i.e.: R C"
        raw_input("Ready?")
        while all([score<score_limit for score in players.values()]):
            p = players.keys()[player_index]
            player_index = (player_index+1)%num_players
            good_choice = False
            print self.board
            while not good_choice:
                choice = raw_input("Player "+p+", place a piece: ").strip()
                try: r, c = map(int, choice.split(" "))
                except Exception:
                    print "Please format as two integers: R C"
                    continue
                if 0 <= r < len(self.board) and 0 <= c < len(self.board[0]):
                    if self.board[r][c] == self.board.default:
                        self.board[r][c] = p
                        squares = get_squares(m.board, (p, Point(r,c)))
                        score = get_scores(squares)
                        players[p] += score.get(p, 0)
                        print "Player",p,"score:",players[p]
                        good_choice = True
                    else: print "That square is occupied."
                else: print "Choice out of range."
        print "Final scores:"
        pprint.pprint(players)

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

    """
    import random
    # try out filling lots of things
    for _ in range(30):
        m.board[random.randint(0,9)][random.randint(0,9)] = 'x'


    print m.board
    squares = get_squares(m.board)
    pprint.pprint(squares)
    scores = get_scores(squares)
    pprint.pprint(scores)

    for _ in range(20):
        p = Point(random.randint(0,9), random.randint(0,9))
        m.board[p.r][p.c] = 'o'
        print m.board
        squares = get_squares(m.board, ('o', p))
        pprint.pprint(squares)
        scores = get_scores(squares)
        pprint.pprint(scores)
    """

    m.run_game()

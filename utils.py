#!/usr/bin/env python
from itertools import combinations

class Point(object):
    def __init__(self, r, c):
        self.r = r
        self.c = c
    def __repr__(self):
        return "Point(" + str(self.r) + ", " + str(self.c) + ")"
    def __ew__(self, other):
        return self.r == other.r and self.c == other.c
    def dist(self, other):
        # NOTE: NOT ACTUAL EUCLIDEAN DISTANCE
        # return the squared distance (to avoid sqrt operation) 
        return (self.r-other.r)**2 + (self.c-other.c)**2

def check_square(S):
    # should verify that all of them have the same character?
    # given S, a list of 4 Point(r,c) objects, decide if square
    # could either use this for actual check or for initially building
    # initial reference
    assert(len(S) == 4)
    # check that there are two 'equal' pairs of equidistant (far) points
    p1, p2, p3, p4 = S
    p1p2 = p1.dist(p2)
    p1p3 = p1.dist(p3)
    if p1p2 == p1p3:
        p2, p4 = p4, p2
    elif p1p2 < p1p3:
        p2, p3 = p3, p2
    # now pairs should be p1,p2 and p3,p4
    if p1.dist(p2) != p3.dist(p4): return False
    # check remaining distances are correct
    if p1.dist(p3) == p1.dist(p4) and p3.dist(p1) == p3.dist(p2) and \
       p2.dist(p3) == p2.dist(p4) and p4.dist(p1) == p4.dist(p2):
        return True
    return False

def get_squares(grid, player_pt=None):
    # Return every found square in a grid
    # might be faster to pre-compute, but...ehhh.
    moves = grid.get_moves()
    # split into different players
    players = dict()
    for pt, player in moves:
        players[player] = players.get(player, []) + [pt]
    # for each, get every combination of 4
    squares = dict()
    # only do one player if necessary 
    if player_pt:
        player, pt = player_pt
        plays = players[player]
        possibilities = [[pt]+list(l) for l in list(combinations(plays, 3))]
        # calculate squares
        for square in possibilities:
            if check_square(square):
                squares[player] = squares.get(player, []) + [list(square)]
    else:
        # otherwise do all players
        for player, plays in players.items():
            possibilities = list(combinations(plays, 4))
            # calculate squares
            for square in possibilities:
                if check_square(square):
                    squares[player] = squares.get(player, []) + [list(square)]
    return squares

def get_square_score(S):
    # get bounding box...are you sure that should be the score?
    p1, p2, p3, p4 = S
    # upper-left corner
    ulx, uly = min([p.r for p in S]), min([p.c for p in S]), 
    # lower-right corner
    lrx, lry = max([p.r for p in S]), max([p.c for p in S]), 
    p1, p2 = Point(ulx, uly), Point(lrx, lry)
    # return area
    return (abs(ulx-lrx)+1)*(abs(uly-lry)+1)

def get_scores(squares):
    scores = {}
    for p,s in squares.items():
        for square in s:
            scores[p] = scores.get(p, 0) + get_square_score(square)
    return scores

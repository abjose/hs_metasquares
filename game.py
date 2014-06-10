#!/usr/bin/env python
from grid import Grid
from utils import Point
import random
import cProfile, pstats, StringIO

class Metasquares(object):

    def __init__(self, r, c):
        self.board = Grid(r, c)
        # should precompute squares on init? or look for file and precompute 
        # if one isn't found

    def get_squares(self, ):
        # Return every found square in the grid
        # might be faster to pre-compute, but don't feel like it
        pass

    def check_square(self, P):
        # should verify that all of them have the same character?
        # given P, a list of 4 Point(r,c) objects, decide if square
        # could either use this for actual check or for initially buildling
        # initial reference
        assert(len(P) == 4)
        # check that there are two 'equal' pairs of equidistant (far) points
        p1, p2, p3, p4 = P
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

if __name__=="__main__":
    # do some get_squares tests
    m = Metasquares(10, 10)
    P = [Point(0,0), Point(0,1), Point(1,0), Point(1,1)]
    print m.check_square(P)
    P = [Point(0,0), Point(0,2), Point(1,0), Point(1,1)]
    print m.check_square(P)
    P = [Point(0,0), Point(0,2), Point(2,0), Point(2,2)]
    print m.check_square(P)
    P = [Point(1,0), Point(0,1), Point(2,1), Point(1,2)]
    print m.check_square(P)


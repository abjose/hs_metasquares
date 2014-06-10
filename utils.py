#!/usr/bin/env python

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"
    def __ew__(self, other):
        return self.x == other.x and self.y == other.y
    def dist(self, other):
        # NOTE: NOT ACTUAL EUCLIDEAN DISTANCE
        # return the squared distance (to avoid sqrt operation) 
        return (self.x-other.x)**2 + (self.y-other.y)**2


def check_square(P):
    # should verify that all of them have the same character?
    # given P, a list of 4 Point(r,c) objects, decide if square
    # could either use this for actual check or for initially building
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

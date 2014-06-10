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

#!/usr/bin/env python
from utils import Point

"""
Make a grid, maintain marks in it, print them out.
Access row r and column c like: Grid[r][c]
"""

"""
TODO:
"""

class Grid(object):

    def __init__(self, r, c, default=" "):
        assert(r > 0 and c > 0)
        self.default = default
        self.grid = [[default for _ in range(c)] for _ in range(r)]

    def __str__(self, ):
        sq_width = 3
        sq_height = 1
        middle_w = int(round(sq_width/2))
        middle_h = int(round(sq_height/2))
        make_border = lambda: "  " + "".join(["+"+"-"*sq_width 
                                       for _ in range(len(self.grid[0]))])+"+\n"
        # print out numbering on top row
        print "    " + (" "*sq_width).join(map(str, range(len(self.grid))))

        output = ""
        for row in range(len(self.grid)):
            output += make_border()
            for i in range(sq_height):
                for col in range(len(self.grid[0])+1):
                    content = " " * sq_width
                    if i == middle_h and col < len(self.grid[0]):
                        # insert character if you in the center of the square
                        content = content[:middle_w]+str(self.grid[row][col])+\
                                  content[middle_w+1:]
                        # add numbering at beginning
                    if i == middle_h and col == 0:
                        output += str(row) + " "
                    output += "|"+content
                output += "\n"
        # one more row
        return output + make_border()

    def __getitem__(self, key):
        return self.grid[key]
    
    def __len__(self):
        return len(self.grid)

    def get_moves(self, ):
        # return all moves (i.e. != default) on the board
        return [(Point(r,c), self.grid[r][c]) 
                for r,row in enumerate(self.grid)
                for c,col in enumerate(row)
                if self.grid[r][c] != self.default]

if __name__=="__main__":
    G = Grid(3, 5)
    G[2][2] = "X"
    G[1][0] = "0"
    print G
    print G.get_moves()

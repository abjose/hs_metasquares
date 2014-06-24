#!/usr/bin/env python
from utils import Point

"""
Make a grid, maintain marks in it, print them out.
Access row r and column c like: Grid[r][c]
"""

"""
TODO:
- consider changing this to use a dictionary instead of a list of lists?
- implement __repr__ for sending over network?
  also need to allow to be constructed from this description
"""

class Grid(object):

    def __init__(self, r=10, c=10, default=" ", load=None):
        assert(r > 0 and c > 0)
        self.default = default
        if load:
            self.load_repr(load)
        else:
            self.init_grid(r, c)            

    def init_grid(self, r, c):
        self.grid = [[self, default for _ in range(c)] for _ in range(r)]

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

    def __repr__(self):
        # Return 'sparse' version of the grid
        # start off with just rows columns
        out = str(len(self.grid)) + "\n" + str(len(self.grid[0])) + "\n"
        # then list all occupied cells
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] != self.default:
                    out += str(r) + ' ' + str(c) + str(self.grid[r][c]) + '\n'
        return out

    def load_repr(self, load):
        # load in output of __repr__ function
        # grab grid size
        load = load.strip().split('\n')
        self.init_grid(int(load[0]), int(load[1]))
        # load in sparse points
        for line in load[2:]:
            line = line.strip().split()
            row, col, mark = int(line[0]), int(line[1]), line[2]
            self.grid[row][col] = mark
        
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

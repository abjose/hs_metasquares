#!/usr/bin/env python
import pprint

"""
Make a grid, maintain marks in it, print them out.
Access row r and column c like: Grid[r][c]
"""

class Grid:

    def __init__(self, r, c, default=" "):
        assert(r > 0 and c > 0)
        self.grid = [[default for _ in range(c)] for _ in range(r)]

    def __str__(self, ):
        sq_width = 7
        sq_height = 3
        middle_w = int(round(sq_width/2))
        middle_h = int(round(sq_height/2))
        make_border = lambda: "".join(["+"+"-"*sq_width 
                                       for _ in range(len(self.grid[0]))])+"+\n"
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
                    output += "|"+content
                output += "\n"
        # one more row
        return output + make_border()

    def display(self, ):
        #pprint.pprint(self.grid)
        print self

    def __getitem__(self, key):
        return self.grid[key]

if __name__=="__main__":
    G = Grid(3, 5)
    G.display()
    G[2][2] = "X"
    G[1][0] = "0"
    print G

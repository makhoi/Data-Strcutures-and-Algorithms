# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        result = -1

        x = rows - 1   # start at bottom row
        y = cols - 1   # start at rightmost column

        while x >= 0 and y >= 0:
            if binaryMatrix.get(x, y) == 1:
                result = y
                y -= 1   # move left
            else:
                x -= 1   # move up

        return result
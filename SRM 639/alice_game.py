class AliceGame():
    def findMinimumValue(self, x, y):
        from math import sqrt
        if not sqrt(x+y).is_integer():
            return -1

class AliceGameEasy():
    def findMinimumValue(self, x, y):
        total = x + y
        turns = 0
        while turns*(turns+1)//2 < total: turns += 1
        
        if turns*(turns+1)//2 > total: return -1
        
        high = 0
        low = 0

        for i in range(turns+1):
            if low <= x <= high: return i
            low += i + 1
            high += turns - i

        return -1
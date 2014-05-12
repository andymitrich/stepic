from sys import stdin
from math import ceil, log
from decimal import Decimal as d

class RMQ(object):
    def __init__(self, numbers):
        self.e = []
        n = len(numbers)
        
        if (n & (n-1))!=0:
            x = ceil(log(n, 2))
            self.n = 2**x;

            while n != self.n:
                numbers.append(d('Infinity'))
                n += 1
            
        for i in range(0, self.n-1, 1):
            numbers.insert(0, min(numbers[self.n-i-1], numbers[self.n-i-2]))

        numbers.insert(0, d('Infinity'))
        self.e = numbers
        self.size = len(numbers)
        # print(self.e)
      
    def recover(self, idx):
        pass
  
    def min(self, left, right, begin = 1, end = None, idx = 1):
        if end is None: end = self.n

        if left==begin and right==end:
            return self.e[idx]

        if left >= begin and right <= end//2:
            # left child
            min(left, right, begin, end//2, 2*idx)
        elif left > end//2 and right <= end:
            min(left, right, end//2, end)
        elif 1:
            return idx+1
        
        
  
    def set(self, origin, value):
        return
        for i in range(self.size//2, self.size-1):

            if self.e[i] == origin:
                self.e[i] = value
                self.recover(i)
        print(self.e)
  
    
if __name__ == '__main__':

    f = open('source/rmq.txt', 'r')
    n, m = map(int, f.readline().split())
    numbers = list(map(int, f.readline().split()))
    # print(n, m)
    rmq = RMQ(numbers)

    # print(numbers)


    for i in range(0, m):
        c, x, y = f.readline().split()

        if c == 'Min':
          print(rmq.min(int(x), int(y)))
        elif c == 'Set':
          rmq.set(x, y)


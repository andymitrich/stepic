#!/usr/local/bin/python3
from sys import stdin
from math import ceil, log
from decimal import Decimal as d

class RMQ(object):
  def __init__(self, numbers):
    self.e = []
    n = len(numbers)
    
    if (n & (n-1))!=0:
      x = ceil(log(n, 2))
      nn = 2**x;
      
      while n != nn:
        numbers.append(d('Infinity'))
        n = len(numbers)
        
    r = numbers[::-1]
    nn = 2*nn-1
    
    self.size = len(numbers)
    
    i = 0
    while i < nn-1:
      r.append(min(r[i], r[i+1]))
      i+=2
      
    r.append(d('Infinity'))
    self.e = r[::-1]

    
  def build(self):
    idx = self.size - 1
    
      
  def recover(self, idx):
    pass
  
  def min(self, left, right):
    pass
  
  def set(self, origin, value):
    for i in range(self.size//2, self.size-1):
      print()
      if self.e[i] == origin:
        self.e[i] = value
        self.recover(i)
    print(self.e)
  
    
if __name__ == '__main__':
  
  f = open('input.txt', 'r')
  n, m = map(int, f.readline().split())
  numbers = list(map(int, f.readline().split()))
  # print(n, m)
  rmq = RMQ(numbers)
    
  # print(numbers)
  
  for i in range(0, m):
    c, x, y = f.readline().split()
    
    if c == 'Min':
      rmq.min(x, y)
    elif c == 'Set':
      rmq.set(x, y)

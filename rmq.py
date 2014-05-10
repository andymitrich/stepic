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
      
    self.size = len()  
    
  def build(self):
    idx = self.size - 1
    while idx > 1:
      self.e[idx//2] = min(self.e[idx], self.e[idx+1])
      idx -= 2
  
  def min(self, left, right):
    pass
  
  def set(self, origin, value):
    pass
  
    
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

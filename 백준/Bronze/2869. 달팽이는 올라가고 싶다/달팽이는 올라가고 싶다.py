import sys
import math

def solve():
  A, B, V = map(int,sys.stdin.readline().split())
  
  
  
  
    
  print(math.ceil(int(V - A)/ int(A - B)) + 1)

solve()
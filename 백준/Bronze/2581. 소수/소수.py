import sys
import math

def solve():
  
  M = int(sys.stdin.readline())
  N = int(sys.stdin.readline())

  sum = 0
  smallestPrime = 0
  atLeastOnePrime = False
  
  for i in range(M,N+1):
    isPrime = True
    if(i > 1):
      for j in range(2, i):
        if(i % j == 0):
          isPrime = False
          break
        
      if(isPrime == True):
        sum += i
        if(atLeastOnePrime == False):
          smallestPrime = i
          atLeastOnePrime = True

  if(atLeastOnePrime == True):
    print(sum)
    print(smallestPrime)
  else:
    print('-1')
  
solve()
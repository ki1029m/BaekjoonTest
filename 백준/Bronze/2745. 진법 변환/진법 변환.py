import sys

def solve():
  N, B = sys.stdin.readline().split(" ")

  B = int(B)

  number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = 0

  for i in range (len(N)):
    sum = number.index(N[i]) * (B ** (len(N)-i-1) )
    result += sum
  
  print(result)

solve()
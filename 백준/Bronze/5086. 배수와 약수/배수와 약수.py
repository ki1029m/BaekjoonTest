import sys
import math

def solve():
  while(1):
    num1, num2 = map(int,sys.stdin.readline().split())
    if(num1 == 0 and num2 == 0):
      break

    if(num1 > num2 and num1 % num2 == 0):
      print('multiple')
      continue
    elif(num1 < num2 and num2 % num1 == 0):
      print('factor')
      continue
    else:
      print('neither')
      
  
solve()
import sys


def solve():
  num = int(sys.stdin.readline())
  d = [0] * (num + 1)
  for i in range(num+1):
    d[i] = [0,0,0]

  d[1][0] = 1
  d[1][1] = 1
  d[1][2] = 1

  for i in range(2, num+1):
    d[i][0] = (d[i-1][1] + d[i-1][2]) % 9901
    d[i][1] = (d[i-1][0] + d[i-1][2]) % 9901
    d[i][2] = (d[i-1][0] + d[i-1][1] + d[i-1][2]) % 9901

  print((d[num][0] + d[num][1] + d[num][2])%9901)

    
    
solve()

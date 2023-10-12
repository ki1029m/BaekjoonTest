import sys

def solve():
  num = int(sys.stdin.readline())
  for i in range(0, num):
    line = sys.stdin.readline().strip().split()
    print('%d' % (int(line[0])+int(line[1])))


solve()

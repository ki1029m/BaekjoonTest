import sys


def solve():
  N, M = map(int,sys.stdin.readline().split())
  arr=[i for i in range(1, 1+N)]
  for i in range(M):
    swap1, swap2 = map(int,sys.stdin.readline().split())
    swap1 -= 1
    swap2 -= 1
    arr[swap1], arr[swap2] = arr[swap2], arr[swap1]

  for i in range(N):
    print(arr[i], end=' ')

solve()

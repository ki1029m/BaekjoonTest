import sys


def solve():
  n, m = map(int,sys.stdin.readline().split()) 

  arr = [[] for i in range(n)]
  visited = [False] * n
  answer = 0

  for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)


  def dfs(idx, cnt):
    nonlocal answer
    
    if cnt == 4:
      answer = 1
      return

    visited[idx] = True
    for i in arr[idx]:
      if not visited[i]:
        dfs(i, cnt+1)
    visited[idx] = False


  for i in range(n):
    dfs(i, 0)
    if answer == 1:
      break

  print(answer)
  
solve()

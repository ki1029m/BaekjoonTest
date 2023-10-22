import sys
# 파이썬은 따로 stack 구조를 제공하지 않음.
# 리스트를 사용

def solve():
    
  n = int(sys.stdin.readline())
  
  stack = []
  for _ in range(n):
    cmd = sys.stdin.readline().split()
  
    if cmd[0] == 'push':
      stack.append(cmd[1])
  
    elif cmd[0] == 'pop':
      if len(stack)==0:
        print(-1)
      else:
        print(stack.pop())
  
    elif cmd[0] == 'size':
      print(len(stack))
  
    elif cmd[0] == 'empty':
      if len(stack)==0:
        print(1)
      else:
        print(0)
    elif cmd[0] == 'top':
      if len(stack)==0:
        print(-1)
      else:
        print(stack[-1])

solve()
  
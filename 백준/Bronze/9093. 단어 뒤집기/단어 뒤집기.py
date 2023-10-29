import sys

#strip()으로 개행문자를 반드시 제거해야함
#스택이용 문제풀이
def solve():
  num = int(sys.stdin.readline())

  for _ in range(num):
    line = sys.stdin.readline().strip()
    line += " "
    stack = []
    for ch in line:
      #공백이 아닐 경우 
      if ch != " ":
        stack.append(ch)
      else:
        while stack:
          print(stack.pop(), end='')
        print(' ', end='')

#파이썬 리스트 이용 문제풀이
def solve2():
  num = int(sys.stdin.readline())
  
  for _ in range(num):
    line = list(sys.stdin.readline().split())
    for word in line:
      print(word[::-1], end=' ')
  

solve()
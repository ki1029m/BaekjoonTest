import sys

#(를 만나면 스택에 저장
#)를 만나면 스택에서 꺼내기

#스택에서 꺼낼 때 없을 경우 조건 충족 X - ')' 가 더 많은 경우
#스택에서 다 꺼냈을 때 남아있는 경우 - '('가 더 많은 경우


def solve():
  num = int(sys.stdin.readline())

  for i in range(num):
    stack = []
    line = sys.stdin.readline().strip()

    for ch in line:
      if ch == '(':
        stack.append(ch)
      elif ch == ')':
        if stack:
          stack.pop()
        else:
          print("NO")
          break
    else:
      if not stack:  # break문으로 안끊기고 스택이 비어있다면 YES
        print("YES")
      else:  # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
        print("NO")


solve()

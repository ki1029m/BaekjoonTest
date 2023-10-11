import sys


def solve2():
  s = sys.stdin.readlines()
  for i in s:
    print(i.rstrip())


def solve():
  while True:
    try:
      s = input()
      print(s)
    except EOFError:
      break


solve()

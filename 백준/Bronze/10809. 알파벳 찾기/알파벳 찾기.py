import sys
import string


def solve():
  S = sys.stdin.readline()
  strings = 'abcdefghijklmnopqrstuvwxyz'
  strings = [i for i in string.ascii_lowercase]
  for i in strings:
    if i in S:
      print(S.index(i), end=' ')
    else:
      print('-1', end=' ')


solve()

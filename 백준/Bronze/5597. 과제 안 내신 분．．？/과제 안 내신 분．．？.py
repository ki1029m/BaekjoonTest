import sys


def solve():
  nums = [i for i in range(1, 31)]

  for i in range(28):
    data = int(sys.stdin.readline())
    nums.remove(data)

  print(min(nums))
  print(max(nums))


solve()

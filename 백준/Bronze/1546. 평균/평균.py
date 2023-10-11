import sys

def solve():
  num = int(sys.stdin.readline())
  scores = list(map(float,sys.stdin.readline().split()))

  max = 0.0
  sum = 0
  for i in range(num):
    sum += scores[i]
    if(max < scores[i]):
      max = scores[i]

  print(sum/float(num) / max * 100)
  

solve()

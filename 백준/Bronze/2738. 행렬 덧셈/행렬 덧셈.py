def solve():
  arrA, arrB = [], []
  
  rows, cols = map(int, input().split())
  
  for row in range(rows):
      row = list(map(int, input().split()))
      arrA.append(row)
  
  for row in range(rows):
      row = list(map(int, input().split()))
      arrB.append(row)
  
  for row in range(rows):
      for col in range(cols):
          print(arrA[row][col] + arrB[row][col], end=' ')
      print()

solve()
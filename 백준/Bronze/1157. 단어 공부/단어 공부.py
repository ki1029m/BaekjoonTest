import sys


def solve():
  s = sys.stdin.readline().upper()
  AtoZ=list()
  for i in range(ord('A'),ord('Z')+1):
    AtoZ.append(chr(i))
  #print(AtoZ)

  wordCount=list()
  for alphabet in AtoZ:
    wordCount.append(s.count(alphabet))
    
  if(wordCount.count(max(wordCount)) > 1):
    print('?')
  else:
    print(AtoZ[wordCount.index(max(wordCount))])
  
  
solve()

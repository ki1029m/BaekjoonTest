import sys

#strip()에서 공백은 제거하면 안되므로 개행문자만 삭제
#소문자 a는 97 z는 122
#대문자 A는 65 Z는 90

#또는 isupper(), islower(), isdigit(), isspace() 사용 가능

#따로 정해진 길이가 없으므로 if (not line): 사용가능


def solve():
  while True :
      s = sys.stdin.readline().strip('\n')
      if not s:
        break
        
      lower = 0
      upper = 0
      number = 0
      blank = 0
    

    
      for i in range(len(s)) :
        if ord('a') <= ord(s[i]) <= ord('z') :
          lower += 1
        elif ord('A') <= ord(s[i]) <= ord('Z') :
          upper += 1
        elif s[i] == ' ' :
          blank += 1
        else :
          number += 1
  
      print(lower, upper, number, blank)


solve()

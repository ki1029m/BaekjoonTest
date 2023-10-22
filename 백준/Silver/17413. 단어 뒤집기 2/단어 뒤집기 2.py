import sys
#rstrip() 함수로 readline에서 받는 \n 개행문자 제거 
#list로 각 문자열 리스트로 변경
#인풋이 숫자, 알파벳 판별시 isalnum() 사용
#뒤집는 함수 reverse() 사용
#join으로 문자열로 변경 "넣고싶은문자".join(list)

def solve():
  input=list(sys.stdin.readline().rstrip())

  i = 0
  start = 0
  end = 0
  
  while(i< len(input)):
    #괄호 시작시 끝날때까지 i이동
    if input[i] == '<':
      i += 1
      while input[i] != '>':
        i += 1
        
    #숫자나 알파벳을 만나면
    #시작과 끝을 알아내어 반전시킨다
    elif input[i].isalnum():
      start = i
      while i < len(input) and input[i].isalnum():
        i +=1
        
      end = i
      rWord = input[start:end]
      rWord.reverse()
      input[start:end] =rWord

    #공백일 경우 그냥 넘어감
    else:
      i+=1

  result = "".join(input)
  print(result)

solve()
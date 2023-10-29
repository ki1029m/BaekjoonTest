import sys

#유클리드 호제법
#두 자연수 a,b에 대하여 a를 b로 나눈 나머지 r에 대해
#a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
#이를 계속 반복하며 b가 0이 될 때, a값이 바로 최대공약수이다


# //는 실수 나누기
# a*b // gcd(a,b) = 최소 공배수

def solve():
  
  a, b = map(int, input().split())

  def gcd(a, b):
      while b > 0:
          a, b = b, a % b
      return a

  def lcm(a, b):
      return a * b // gcd(a, b)

  print(gcd(a, b))
  print(lcm(a, b))


solve()

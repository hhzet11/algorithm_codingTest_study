T = int(input())

def factorial(n):
  num = 1
  for i in range(1, n+1):
    num *= i
  return num

while T > 0:
  T = T-1
  n, m = map(int, input().split())
  result = factorial(m) // (factorial(m-n) * factorial(n))

  print(result)

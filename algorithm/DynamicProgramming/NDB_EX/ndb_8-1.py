# 8-1. 피보나치 함수
# 피보나치 함수를 재귀 함수로 구현
def fibo(x):
  # 피보나치 수열에서 첫 번째 항, 두 번째 항의 값 모두 1
  if x == 1 or x == 2:
    return 1
  return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
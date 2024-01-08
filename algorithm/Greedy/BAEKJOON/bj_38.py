# 14916번 거스름돈 (실버5) 240107 - 그리디 🔼
def solution():
  n = int(input())  # 거스름돈 액수
  result = 0

  # 거스름돈이 1, 3인 경우 거슬러 줄 수 없음
  if n == 1 or n == 3:
    print(-1)
  else:
    while n > 0:
      if n % 5 == 0:
        result += n // 5
        n %= 5
      else:
        result += 1
        n -= 2
    print(result)

  # 코드 출처 : https://velog.io/@tunaman95/%EB%B0%B1%EC%A4%80-14916%EB%B2%88-%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88-Python
  # while n > 0:
  #   if n % 5 == 0:
  #     result += n // 5
  #     n %= 5
  #   else:
  #     result += 1
  #     n -= 2

  # # n이 0으로 딱 떨어지지 않았을 경우 거슬러 줄 수 없음
  # if n < 0:
  #   print(-1)
  # else:
  #   print(result)

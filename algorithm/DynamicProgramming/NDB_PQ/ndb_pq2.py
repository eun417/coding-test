# 실전문제 2. 개미전사 (교재 코드)
def solution() :
  # 정수 N 입력받기
  n = int(input())
  # 모든 식량 정보 입력받기
  array = list(map(int, input().split())) 

  # 식량창고의 개수는 3 <= N <= 100 이므로
  # dp의 n번째 값은 n번째까지 고른 최대값의 합이 되도록 채우기
  # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
  dp = [0] * 100

  # 다이나믹 프로그래밍 진행 (보텀업)
  # dp[0] -> k[0]
  # dp[1] -> k[0], k[1] 중 더 큰 것
  dp[0] = array[0]
  dp[1] = max(array[0], array[1])

  for i in range(2, n) :
    # i번째를 고르게되면 i의 식량과 i-2의 합이 됨
    # i-1번째를 고르게되면 i의 값은 i-1 값이 됨
    dp[i] = max(dp[i-1], dp[i-2] + array[i])

  #계산된 결과 출력
  print(dp[n-1])
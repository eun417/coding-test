#좌표 압축 (실버2) 231214 ❎ ... 시간초과
def solution() :
  import sys
  input = sys.stdin.readline
  
  n = int(input())  #좌표 개수
  x_list = list(map(int, input().split()))  #입력받은 좌표 리스트
  c_list = [0] * n  #압축된 좌표 리스트

  for i in range(n) :
    start = x_list[i]  #압축 시작점
    count = 0  #압축된 좌표 개수

  for i in range(n) :
    tmp = 10**9+1  #입력값 범위인 10^9 넘어가는 수 임시 저장
    count = 0  #조건 만족하는 서로 다른 좌표 개수
    for j in range(n) :
      #이전에 count 했을 때와 동일한 수는 count 하지 않음
      if x_list[i] > x_list[j] and x_list[j] != tmp :
        tmp = x_list[j] 
        count += 1
        c_list[i] = count
      else :
        c_list[i] = count
  
  #결과 출력
  print(*c_list)
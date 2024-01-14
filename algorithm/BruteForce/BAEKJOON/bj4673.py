# 4673번 셀프 넘버 (실버5) 240124 - 완전탐색 ✅ ... 시간초과
def solution():
  # 셀프 넘버 = 생성자 없는 숫자
  for i in range(1, 10001):
    x = 0
    for j in range(1, 10001):
      num_sum = j + sum(map(int, str(j)))
      if num_sum == i:
        x = i
        break
    if i != x:
      print(i)
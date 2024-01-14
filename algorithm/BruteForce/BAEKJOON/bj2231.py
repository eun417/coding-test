# 2231번 분해합 (브론즈2) 240114 - 완전탐색
def solution() :
  n = int(input())  #자연수
  const = n
  arr = []
  while const > 0 :
    const -= 1
    div_sum = sum(map(int, str(const)))
    if n == const + div_sum :
      arr.append(const)

  # 생성자 없는 경우
  if not arr :
    print(0)
  else :
    print(min(arr))
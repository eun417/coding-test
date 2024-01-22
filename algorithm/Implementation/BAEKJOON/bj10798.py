# 10798번 세로읽기 (브론즈1) 240122 - 구현 🅾
# 런타임에러(IndexError)1회
def solution():
  str = []
  for _ in range(5):
    str.append(list(input()))

  # 각 줄의 글자 범위 최소 1개 ~ 최대 15개
  for i in range(15):
    for j in str:
      # 인덱스 넘어가면 다시 조건으로 돌아감
      if len(j) <= i:
        continue
      else:
        print(j[i], end='')

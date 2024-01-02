# 단어의 개수 (브론즈2) 240102 🅾
def solution():
  import sys
  input = sys.stdin.readline

  count = 0  # 단어 개수 (*결과값)

  # 문자열 입력받기
  for i in input().split():
    # 공백 하나만 입력으로 주어진 경우 count 하지 않음
    if i == ' ':
      continue
    else:
      count += 1

  print(count)

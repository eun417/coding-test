def solution() :
  m = int(input()) #컵 위치 바꾼 횟수
  result = 1 #공이 있는 컵 위치
  
  for _ in range(m) :
    x, y = map(int, input().split()) #위치 바꿀 컵

    if x == result :
      x, y = y, x #위치 바꿈
      result = x
    elif y == result:
      x, y = y, x #위치 바꿈
      result = y
    
  print(result)
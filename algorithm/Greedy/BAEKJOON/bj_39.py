# 2828번 사과 담기 (실버5) 240107 - 그리디
def solution() :
  n, m = map(int, input().split())  # n: 스크린 칸 수, m: 바구니 칸 수
  j = int(input())
  
  result = 0  #바구니가 이동해야 하는 거리 최솟값 (*결과값)

  ml = 1  # 바구니 왼쪽 위치
  mr = m  # 바구니 오른쪽 위치
  
  for i in range(j) :
    al = int(input())  # 사과가 떨어지는 위치
    # al이 ml보다 크면 오른쪽으로 바구니를 움직임
    if mr < al :  
      ml = al - m + 1  # 사과가 떨어지는 위치에서 바구니 크기를 빼고 +1
      mr = al  # 바구니 오른쪽 위치는 사과가 떨어지는 위치와 같음 
      result += ml
    # al이 ml보다 작으면 왼쪽으로 바구니를 움직임
    elif ml > al : 
      mr = ml - al - 1  # 바구니 왼쪽 위치에서 사과가 떨어지는 위치를 빼고 -1
      ml = al  # 바구니 왼쪽 위치는 사과가 떨어지는 위치와 같음
      result += mr
  
  print(result)
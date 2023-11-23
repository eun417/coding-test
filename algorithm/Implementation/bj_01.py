def solution() :
  n, m = map(int, input().split()) #행:m, 열: n
  ball_list = [0]*n

  for a in range(m) :
    i, j, k = map(int, input().split())
    for b in range(i-1, j) :
      ball_list[b] = k
  
  print(*ball_list) 
  
  #
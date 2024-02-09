# 1789번: 수들의 합 (실버5) 240209 - 그리디 ✳
def solution() :
  s = int(input())  # 서로 다른 n개의 자연수의 합

  sum = 0
  n = 0
  for i in range(1, s+1) :
    sum += i
    if sum > s :
      break
    else :
      n += 1
      
  print(n)
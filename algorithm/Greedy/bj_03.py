#ATM (231119)
def atm() :
  n = int(input()) #사람의 수
  p = list(map(int, input().split())) #돈 인출 시간
  result = 0 #필요한 시간 합 최솟값
  
  p.sort()

  for i in range(len(p)) :
    result += p[i]*n
    n -= 1
    # p[0]*5 + p[1]*4 + p[2]*3 + p[3]*2 + p[4]*1

  print(result)
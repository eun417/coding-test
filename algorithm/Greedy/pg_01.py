#01 체육복 (231121)
def sportswear(n, lost, reserve) :
  result = n - len(lost) #체육수업 들을 수 있는 학생 최댓값 ... 기본값 설정

  lostCount = len(lost)
  reserveCount = len(reserve)
  for i in range(n) :
    if lostCount == 0 or reserveCount == 0 :
      break
    elif lost[i]-reserve[i] == 1 or lost[i]-reserve[i] ==-1 :
      result += 1
      lostCount -= 1
      reserveCount -= 1
    else :
      break

  print(result)
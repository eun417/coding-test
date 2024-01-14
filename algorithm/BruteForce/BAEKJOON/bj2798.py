# 2898번 블랙잭 (브론즈2) 240114 - 완전탐색
def solution() :
  n, m = map(int, input().split())  #n: 카드 개수, m: 딜러가 외친 수
  cards = list(map(int, input().split()))  #카드

  minus = []
  result = 0
  # cards[0] + cards[1] + cards[2]
  # cards[0] + cards[1] + cards[3]
  # cards[0] + cards[1] + cards[4]
  # cards[0] + cards[2] + cards[3]
  # cards[0] + cards[2] + cards[4]
  # cards[0] + cards[3] + cards[4]
  for i in range(n) :
    for j in range(i+1, n) :
      for h in range(j+1, n) :
        sum = cards[i] + cards[j] + cards[h]
        if m - sum >= 0 :
          minus.append(m - sum)

  result = m - min(minus)  #m에 가장 가까운 수
  
  print(result)
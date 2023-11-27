#카드 역배치 (231127)
def solution() :
  card_list = [c for c in range(1, 21)] #카드 리스트
  
  for _ in range(10) :
    a, b = map(int, input().split()) #a~b 구간
    tmp = card_list[a-1:b] #역순할 구간 임시 저장
    tmp.reverse()
    card_list[a-1:b] = tmp

  print(*card_list)
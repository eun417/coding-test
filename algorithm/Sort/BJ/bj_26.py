#숫자 카드 2 (실버4) 231215 ✅ ... 시간 초과
def solution() :
  import sys
  input = sys.stdin.readline
  
  n = int(input())  #상근이가 가지고 있는 숫자 카드 개수
  cards = list(map(int, input().split()))  #숫자 카드에 적힌 정수

  m = int(input())  #상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 수
  target = list(map(int, input().split()))  

  cards_count = [0] * len(target)

  for i in range(len(target)) :
    if target[i] in cards :  #target인 카드가 cards 안에 있다면
      cards_count[i] = cards.count(target[i])  #그 카드 개수 세기

  print(*cards_count)
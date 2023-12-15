#숫자 카드 2 (실버4) 231215 ✳
#다른 사람 코드 참고함 ... 제출 X
def solution() :
  import sys
  input = sys.stdin.readline
  
  n = int(input())  #상근이가 가지고 있는 숫자 카드 개수
  cards = list(map(int, input().split()))  

  m = int(input())  #상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 수
  target = list(map(int, input().split()))  

  cards_count = {}  #카드 개수 저장할 딕셔너리
  for i in target:
    #target의 각 숫자에 대해 카드 개수를 0으로 초기화
    cards_count[i] = 0

  for i in cards:
    if i in cards_count:  #만약 딕셔너리 안에 겹치는 cards가 있다면
      cards_count[i] += 1  #카드 개수 +1

  #결과 출력
  for i in cards_count:
    print(cards_count[i], end=' ')
#숫자 카드 (실버5) 231216 🅾 ... 시간복잡도 신경써야 될 듯!
def solution():
  def binary_search(array, target, start, end):
    while start <= end:
      mid = (start + end) // 2  #중간점 인덱스
      if array[mid] == target:
        return mid
      #찾고자 하는 값이 중간점의 값보다 작은 경우
      elif array[mid] > target:
        end = mid - 1
      else :
      #찾고자 하는 값이 중간점의 값보다 큰 경우
        start = mid + 1

    return None
    
  import sys
  input = sys.stdin.readline

  n = int(input())  #상근이가 가진 숫자 카드 개수
  cards = list(map(int, input().split()))  #카드에 적힌 정수
  m = int(input())  #확인할 카드 개수
  check_cards = list(map(int, input().split()))  #확인할 카드에 적힌 정수

  cards.sort()  #카드 정렬

  for i in check_cards:
    result = binary_search(cards, i, 0, n-1)
    if result == None:
      print(0, end=' ')
    else :
      print(1, end=' ')
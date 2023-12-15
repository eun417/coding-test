#실전문제 1. 부품 찾기 (내 코드)
def solution() :
  #이진탐색 구현(재귀함수)
  def binary_search(store, customer, start, end):
    if start > end:
      return None

    mid = (start+end) // 2  #중간점

    #찾고자 하는 값이 중간점의 값과 같은 경우
    if store[mid] == customer:
      return mid
    #찾고자 하는 값이 중간점의 값보다 작은 경우
    elif store[mid] > customer:
      return binary_search(store, customer, start, mid-1)
    #찾고자 하는 값이 중간점의 값보다 큰 경우
    else:
      return binary_search(store, customer, mid+1, end)
  
  import sys
  input = sys.stdin.readline
  
  n = int(input())  #가게 부품 개수
  store = list(map(int, input().split()))
  store.sort()  #이진탐색을 위해 사전에 정렬 수행
  m = int(input())  #손님이 문의한 부품 개수
  customer = list(map(int, input().split()))

  for i in customer:
    result = binary_search(store, i, 0, n-1)
    if result == None:
      print('no', end=' ')
    else :
      print('yes', end=' ')
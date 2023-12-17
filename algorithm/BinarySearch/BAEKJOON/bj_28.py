#수 찾기 (실버4) 231216 🅾 464ms
def solution() :
  def binary_search(array, target, start, end):
    while start <= end:
      mid = (start+end) // 2
  
      #확인할 값과 리스트 중간점의 값이 같은 경우
      if array[mid] == target:
        return 1
      #확인할 값이 리스트 중간점의 값보다 작은 경우
      elif array[mid] > target:
        end = mid - 1
      #확인할 값이 리스트 중간점의 값보다 큰 경우
      else:
        start = mid + 1
  
    return 0
    
  import sys
  input = sys.stdin.readline
  
  n = int(input())  #정수 개수
  a_list = list(set(map(int, input().split())))  #정수
  m = int(input())  #확인할 정수 개수
  
  a_list.sort()  #정렬
  
  #결과 출력
  for i in input().split():
    print(binary_search(a_list, int(i), 0, len(a_list)-1))
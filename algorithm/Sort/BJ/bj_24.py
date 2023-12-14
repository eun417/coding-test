#좌표 정렬하기 (실버5) 231214 🅾
def solution() :
  import sys
  input = sys.stdin.readline
  
  n = int(input())  #점의 개수
  list = []
  for i in range(n) :
    x, y = map(int, input().split())  #좌표
    list.append((x, y))
  
  list.sort()  #정렬
  
  #결과 출력
  for i in list :
    print(i[0], i[1])
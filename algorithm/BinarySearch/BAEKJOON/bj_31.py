#나무 자르기 (실버2) 231217 ✳ 4628ms ... 시간 너무 오래 걸림
def solution() :
  import sys
  input = sys.stdin.readline

  n, m = map(int, input().split())  #나무의 수, 상근이가 가질 나무의 길이
  tree_list = list(map(int, input().split()))  #나무의 높이

  start = 0
  end = max(tree_list)  #가장 긴 나무 높이

  while start <= end :
    mid = (start+end) // 2
    total = 0

    for tree in tree_list :
      #나무 높이가 절단기 높이보다 큰 경우
      if tree > mid :
        total += (tree - mid)  #나무 자름

    #자른 나무들의 길이가 m 이상인 경우
    if total >= m :
      start = mid + 1
    #m보다 작은 경우
    else :
      end = mid - 1

  print(end)
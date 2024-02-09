#2417번: 정수 제곱근 (실버4) 240209 - 수학/이분 탐색 ✅
#틀림 ... 조건을 잘못 나눈 것 같은데 뭘까?
def solution() :
  n = int(input())

  mid = 0
  start = 1
  end = n
  
  while start <= end :
    mid = (start + end) // 2 
    mid_square = mid ** 2
    if mid_square < n :
      start = mid + 1
    elif mid_square > n :
      end = mid - 1
    else :
      break

  print(mid)
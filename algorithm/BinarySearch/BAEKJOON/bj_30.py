#먹을 것인가 먹힐 것인가 (실버3) 231217 ✅ ... 예제는 맞는데 틀림
def solution() :
  def binary_search(b_list, target, start, end) :
    count = 0

    while start <= end :
      mid = (start+end) // 2

      #A의 크기가 B의 중간점의 값보다 큰 경우
      if b_list[mid] <= target :
        count += 1  #카운트
        start = mid + 1 

      #A의 크기가 B의 중간점의 값보다 작거나 같은 경우
      else :
        end = mid - 1  

    return count

  import sys
  input = sys.stdin.readline

  t = int(input())  #테스트 케이스 개수
  for _ in range(t) :
    n, m = map(int, input().split())  #A의 수, B의 수
    a_list = sorted(map(int, input().split()))  #A의 크기
    b_list = sorted(map(int, input().split()))  #B의 크기

    result = 0
    for i in a_list :
      result += binary_search(b_list, i, 0, m-1)
    print(result)
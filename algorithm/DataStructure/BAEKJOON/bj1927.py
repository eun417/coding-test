# 1927번: 최소 힙 (실버2) 240123 - 자료구조/우선순위 큐 ✳
# PriorityQueue 인터넷 참고 -> 제출 X
def solution() :
  import sys
  input = sys.stdin.readline

  from queue import PriorityQueue
  queue = PriorityQueue()

  for _ in range(int(input())) :
    x = int(input())
    
    if x == 0 :
      # 큐의 사이즈 반환
      if queue.qsize() == 0 :
        print(0)
      else :
        # 원소 삭제 (오름차순)
        print(queue.get())
    else :
      # x 원소 추가
      queue.put(x)

  # 리스트로 구현 -> 시간 초과
  # queue = []
  # for _ in range(int(input())) :
  #   x = int(input())

  #   if x == 0 :
  #     if len(queue) == 0 :
  #       print(0)
  #     else :
  #       queue.sort()
  #       print(queue.pop(0))
  #   else :
  #     queue.append(x)
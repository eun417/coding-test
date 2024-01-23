# 10845번 큐 (실버4) 2400123 - 자료구조/큐
def solution() :
  import sys
  input = sys.stdin.readline
  
  from collections import deque
  queue = deque()
  
  for _ in range(int(input())) :
    command = input().split()
    
    if command[0] == 'push' :
      queue.append(command[1])
    elif command[0] == 'pop' :
      if not queue :
        print(-1)
      else :
        print(queue.popleft())
    elif command[0] == 'size' :
      print(len(queue))
    elif command[0] == 'empty' :
      if not queue :
        print(1)
      else :
        print(0)
    elif command[0] == 'front' :
      if not queue :
        print(-1)
      else :
        print(queue[0])
    elif command[0] == 'back' :
      if not queue :
        print(-1)
      else :
        print(queue[len(queue)-1])
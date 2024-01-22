# 10828번 스택 (실버4) 240122 - 구현/자료구조/스택 🅾
def solution() :
  import sys
  input = sys.stdin.readline

  stack = []

  order = ['push', 'pop', 'size', 'empty', 'top']

  for _ in range(int(input())) :
    o = input().split()

    if o[0] == order[0] :  # push
      stack.append(o[1])
    elif o[0] == order[1] :  # pop
      if not stack :
        print(-1)
      else :
        print(stack.pop())
    elif o[0] == order[2] :  # size
      print(len(stack))
    elif o[0] == order[3] :  # empty
      if not stack :
        print(1)
      else :
        print(0)
    elif o[0] == order[4] :  # top
      if not stack :
        print(-1)
      else :
        print(stack[len(stack)-1])
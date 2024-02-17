#1343번: 폴리오미노 (실버5) 240217 - 구현/그리디
def solution() :
  board = list(input())

  x_count = 0
  for i in range(len(board)) :
    if board[i] == 'X' :
      x_count += 1

    if board[i] == '.' or i == (len(board)-1) :
      #X 개수가 홀수인 경우
      if x_count % 2 != 0 :
        print(-1)
        return
      else :
        x_count = 0

  x_count = 0
  for i in range(len(board)) :
    if board[i] == 'X' :
      x_count += 1

    if board[i] == '.' or i == (len(board)-1) :
      while x_count > 0 :
        if x_count % 4 == 0 or x_count // 2 > 1 :
          print('AAAA', end='')
          x_count -= 4
        else :
          print('BB', end='')
          x_count -= 2

      if board[i] == '.' :
        print('.', end='')

solution()
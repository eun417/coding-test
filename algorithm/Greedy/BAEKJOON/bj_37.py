# 1343번 폴리오미노 (실버5) 240107 - 그리디 ❎
# 코드 출처 : @jkethics
def solution():
  import sys
  input = sys.stdin.readline

  # 보드판 입력
  board = input().replace('XXXX', 'AAAA').replace('XX', 'BB')

  # X가 0이 아니면 -1 출력
  if board.count('X') != 0:
    print(-1)
  else:
    print(board)

  # for i in range(len(board)) :
  #   x_count = board[:i].count('X')
  #   if board[i] == '.' or i == len(board)-1:
  #     if x_count % 4 == 0 :
  #       for j in range(i) :
  #         board[j] = 'A'
  #     elif x_count % 2 == 0 :
  #       for j in range(i) :
  #         board[j] = 'B'

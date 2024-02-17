#14940: 쉬운 최단거리 (실버1) 240217 ✳ - 그래프 이론/그래프 탐색/BFS 
def solution() :
  import sys
  from collections import deque
  input = sys.stdin.readline
  
  n, m = map(int, input().split())
  board = [list(map(int, input().split())) for _ in range(m)]

  #목표 지점 찾기
  x, y = 0, 0
  for i in range(n) :
    for j in range(m) :
      if board[i][j] == 2 :
        x, y = i, j

  #상하좌우
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]

  queue = deque()
  queue.append((x, y))

  while queue :
    x, y = queue.popleft()

    #현재 위치에서 네 방향으로의 위치 확인
    for i in range(4) :
      nx = dx[i] + x
      ny = dy[i] + y

      #미로 찾기 공간을 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m :
        continue

      #벽인 경우 무시
      if board[nx][ny] == 0:
        continue

      #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if board[nx][ny] == 1 :
        board[nx][ny] = board[x][y] + 1
        queue.append((nx, ny))

  #지도 출력
  for i in range(n) :
    for j in range(m) :
      #0은 그대로 출력
      if board[i][j] == 0 :
        print(board[i][j], end=' ')
      #거리 출력을 위해 -2
      else :
        print(board[i][j] - 2, end=' ')
    print()
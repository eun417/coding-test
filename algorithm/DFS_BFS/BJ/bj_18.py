#[백준] 단지 번호 붙이기 (실버1) 231208 ❎
#안 풀린다 ... 나중에 다시 풀기
#총 단지 수는 구했는데, 각 단지내 집의수를 못 구함
def solution():
  n = int(input())  #지도의 크기

  graph = []
  for _ in range(n):
    graph.append(list(map(int, input())))

  # print(graph)

  #총 단지 수 (*결과값)
  complex = 0

  #DFS
  def dfs(x, y):
    global complex

    if x <= -1 or x >= n or y <= -1 or y >= n:
      return False

    if graph[x][y] == 1:
      graph[x][y] = 2
      dfs(x - 1, y)
      dfs(x, y - 1)
      dfs(x + 1, y)
      dfs(x, y + 1)
      # for i in range(n):
      #   for j in range(n):
      #     print(graph[i][j], end=' ')
      #   print()
      # print('-----------------')
      return True

    return False

  for i in range(n):
    for j in range(n):
      if dfs(i, j) == True:
        complex += 1

  for i in range(n):
    for j in range(n):
      print(graph[i][j], end=' ')
    print()
  print('complex:', complex)

  # dx = [-1, 0, 1, 0]
  # dy = [0, -1, 0, 1]

  # #BFS
  # def bfs(x, y) :
  #   from collections import deque

  #   queue = deque()
  #   queue.append((x, y))

  #   while queue :
  #     x, y = queue.popleft()
  #     for i in range(4) :
  #       nx = x + dx[i]
  #       ny = y + dy[i]

  #       if nx < 0 or ny < 0 or nx >= n or ny >= n :
  #         continue

  #       if graph[nx][ny] == 0 :
  #         continue

  #       if graph[nx][ny] == 1:
  #         graph[nx][ny] = graph[x][y]
  #         queue.append((nx, ny))
  #         print('queue:', queue)
  #         for i in range(n) :
  #           for j in range(n) :
  #             print(graph[i][j], end=' ')
  #           print()
  #       complex

  #   return graph[x][y]

  # print(bfs(0, 0))

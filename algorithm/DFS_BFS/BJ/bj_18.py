#[백준] 단지 번호 붙이기 (실버1) 231208 ❎ 231211 🅾
#231208/ 안 풀린다 ... 나중에 다시 풀기
#총 단지 수는 구했는데, 각 단지내 집의수를 못 구함
#231211/ 풀었다... GPT의 도움을 받아서 제출은 하지 않음 !!
def solution():
  import sys
  sys.setrecursionlimit(10**5)  #재귀 깊이 제한 변경

  n = int(input())  #지도의 크기

  graph = []  #아파트 단지
  for _ in range(n):
    graph.append(list(map(int, input())))

  complex_count = 0  #총 단지 수 (*결과값)
  house_count = []  #각 단지내 집의 수 (*결과값)

  #방향 벡터
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  #DFS
  def dfs(x, y):
    global complex_count
    global house_count

    if x <= -1 or x >= n or y <= -1 or y >= n:
      return False

    if graph[x][y] == 1:
      graph[x][y] = 2  # 방문한 집을 2로 표시
      house_count[complex_count] += 1  #각 단지내 집의 수 카운트
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)
      return True

    return False

  #house_count 리스트 초기화
  for _ in range(n):
    house_count.append(0)

  for i in range(n):
    for j in range(n):
      if dfs(i, j):
        complex_count += 1

  print(complex_count)

  for i in range(complex_count):
    print(house_count[i])

  # for i in range(n):
  #   for j in range(n):
  #     print(graph[i][j], end=' ')
  #   print()

  # #방향 벡터
  # dx = [-1, 0, 1, 0]
  # dy = [0, -1, 0, 1]

  # #BFS
  # def bfs(x, y) :
  #   from collections import deque

  #   count = 0

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
  #         graph[nx][ny] = count
  #         queue.append((nx, ny))
  #         count += 1

  #   return count

  # for i in range(n):
  #   for j in range(n):
  #     bfs(i, j)

  # for i in range(n):
  #   for j in range(n):
  #     print(graph[i][j], end=' ')
  #   print()

  # print('all_count:', all_count)
  # print('count:', count)

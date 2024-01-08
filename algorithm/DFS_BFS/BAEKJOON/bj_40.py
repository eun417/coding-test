# 4963번 섬의 개수 (실버2) 240108 - DFS&BFS ✳
def solution():
  import sys
  sys.setrecursionlimit(10**6)  # 최대 재귀 깊이 1,000,000으로 제한

  def dfs(x, y):
    # 주어진 범위 벗어나면 즉시 종료
    if x <= -1 or x >= h or y <= -1 or y >= w:
      return False

    if graph[x][y] == 1:
      graph[x][y] = 2
      # 상하좌우
      dfs(x - 1, y)
      dfs(x, y - 1)
      dfs(x + 1, y)
      dfs(x, y + 1)
      # 대각선
      dfs(x - 1, y - 1)
      dfs(x + 1, y + 1)
      dfs(x - 1, y + 1)
      dfs(x + 1, y - 1)
    else:
      return False

  while True:
    w, h = map(int, input().split())  # w: 지도 너비, h: 지도 높이
    if w == 0 and h == 0:
      break
    graph = [list(map(int, input().split())) for _ in range(h)]  # 지도
    result = 0  # 섬의 개수 (*결과값)

    # dfs 호출
    for i in range(h):
      for j in range(w):
        # 섬이 아닌 곳은 False
        if dfs(i, j) is not False:
          result += 1

    print(result)

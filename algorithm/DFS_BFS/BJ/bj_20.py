#유기농 배추 (실버2) 231211 🅾
def solution() :
  import sys
  sys.setrecursionlimit(10 ** 6)  #재귀 깊이 제한 변경
  
  t = int(input())  #테스트 케이스 개수
  
  #DFS
  def dfs(x, y, graph) :
    #조건 설정 잘못해서 런타임 에러 6번 나옴 ...
    if x <= -1 or x >= n or y <= -1 or y >= m :
      return False
  
    if graph[x][y] == 1 :
      graph[x][y] = 2  #방문 확인용
      dfs(x+1, y, graph)
      dfs(x-1, y, graph)
      dfs(x, y+1, graph)
      dfs(x, y-1, graph)
      return True
  
    return False
  
  for _ in range(t) :
    m, n, k = map(int, sys.stdin.readline().strip().split())  #가로, 세로, 배추 위치 개수
    graph = [[0] * m for _ in range(n)]  #배추밭
    for _ in range(k) :
      x, y = map(int, sys.stdin.readline().strip().split())  #배추 위치
      graph[y][x] = 1  #배추 위치에 배추 심기
  
    count = 0  #배추흰지렁이 수 (*결과값)
  
    for i in range(n) :
      for j in range(m) :
        if dfs(i, j, graph) :
          count += 1
  
    print(count)
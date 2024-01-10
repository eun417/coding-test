# 11725번 트리의 부모 찾기 (실버2) 240110 - DFS&BFS ✳
def solution() :
  import sys
  input = sys.stdin.readline
  sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한 설정

  n = int(input())  # 노드 개수
  graph = [[] for _ in range(n+1)]
  for _ in range(n-1) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

  # 부모노드 리스트 (*결과값)
  parentList = [[] for _ in range(n+1)]  

  def dfs(graph, v, visited) :
    visited[v] = True
    for i in graph[v] :
      if not visited[i] :
        # 부모노드와 연결된 노드를 방문하면 부모노드 저장
        parentList[i] = v   
        dfs(graph, i, visited)

  # 방문정보 저장
  visited = [False] * (n+1)

  # DFS 실행
  dfs(graph, 1, visited)

  # 부모노드 출력
  for i in range(2, n+1) :
    print(parentList[i])
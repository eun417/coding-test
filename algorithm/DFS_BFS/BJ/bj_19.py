#연결요소의 개수 (실버2) 231208, 231211
import sys
sys.setrecursionlimit(10 ** 5)

def solution() :
  n, m = map(int, sys.stdin.readline().split())  #정점 개수, 간선 개수
  graph = [[] for _ in range(n+1)]
  for _ in range(m) :
    u, v = map(int, sys.stdin.readline().split())  #간선의 양 끝점
    graph[u].append(v)
    graph[v].append(u)

  count = 0  #연결요소 개수 (*결과값)

  visited = [False] * (n+1)  #방문 정보 리스트

  #DFS
  def dfs(graph, v, visited) :
    visited[v] = True

    for i in graph[v] :
      if not visited[i] :
        dfs(graph, i, visited)

  for i in range(1, len(visited)) :
    #모든 노드를 방문하도록 함
    if visited[i] is False :
      count += 1
      dfs(graph, i, visited)

  print(count)
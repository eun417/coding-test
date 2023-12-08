#[백준] 바이러스 (실버3) 231208 🅾
def solution():
  n = int(input())  #컴퓨터의 수
  pn = int(input())  #컴퓨터 쌍의 수

  #네트워크 상 연결된 컴퓨터 쌍의 정보
  graph = [[] for i in range(n + 1)]
  for _ in range(pn):
    a, b = map(int, input().split())
    #연결되어 있으면 모두 바이러스 걸리니까 양방향 고려
    graph[a].append(b)
    graph[b].append(a)

  #방문 정보 리스트
  visited = [False] * (n + 1)

  #DFS
  def dfs(graph, v, visited):
    visited[v] = True  #현재 방문 중인 노드 방문 처리

    for i in graph[v]:
      if not visited[i]:
        dfs(graph, i, visited)

    #1번 컴퓨터를 통해 방문한 컴퓨터의 수(= 바이러스 걸리게 되는 컴퓨터 수)
    return sum(visited) - 1

  #DFS 호출
  print(dfs(graph, 1, visited))

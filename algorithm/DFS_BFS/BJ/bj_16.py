#DFS와 BFS (실버2) 231207
#이코테에 있는 코드들을 참고해서 풀었다. 
#내 힘만으로 푼 건 아니라서 답안 제출은 하지 않았다!

def solution() :
  #n: 정점의 개수, m: 간선의 개수, v: 탐색을 시작할 정점의 번호
  n, m, v = list(map(int, input().split()))

  graph = [[] for i in range(n+1)]
  for i in range(m) :
    a, b = list(map(int, input().split()))
    #양방향이므로 a버전, b버전 만듦
    graph[a].append(b)
    graph[b].append(a)
    #정렬
    graph[a].sort()
    graph[b].sort()

  # print('graph:', graph)

  #DFS 메소드 정의
  def dfs(graph, v, visited) :
    #현재 노드 방문 처리
    visited[v] = True
    print(v, end = ' ')  #방문한 순서대로 노드 출력
    
    for i in graph[v] :
      if not visited[i] :  #이미 방문한 적 없는 경우
        dfs(graph, i, visited)

  #BFS 메소드 정의
  def bfs(graph, v, visited) :
    from collections import deque
    
    queue = deque([v])
    
    #현재 노드를 방문 처리
    visited[v] = True
    
    while queue :
      v = queue.popleft()
      print(v, end = ' ')

      #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
      for i in graph[v] :
        if not visited[i] :
          queue.append(i)
          visited[i] = True

  #방문 정보 저장할 리스트
  visited = [False] * (n+1)
  
  #DFS 호출
  dfs(graph, v, visited)

  print()  #줄바꿈

  #방문 정보 저장할 리스트
  visited = [False] * (n+1)
  
  #BFS 호출
  bfs(graph, v, visited)
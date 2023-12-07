#이코테 - DFS/BFS 예제 모음


#5-1. 스택 예제
def ex1():
  stack = []

  #삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
  stack.append(5)
  stack.append(2)
  stack.append(3)
  stack.append(7)
  stack.pop()
  stack.append(1)
  stack.append(4)
  stack.pop()

  print(stack)  #최하단 원소부터 출력
  print(stack[::-1])  #최상단 원소부터 출력


#5-2. 큐 예제
def ex2():
  from collections import deque

  #큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque()

  #삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
  queue.append(5)
  queue.append(2)
  queue.append(3)
  queue.append(7)
  queue.popleft()  #선입선출
  queue.append(1)
  queue.append(4)
  queue.popleft()

  print(queue)  #먼저 들어온 순서대로 출력
  queue.reverse()  #다음 출력을 위해 역순으로 바꾸기
  print(queue)  #나중에 들어온 원소부터 출력


#5-3. 재귀 함수 예제
def ex3():

  def recursive_function():
    print('재귀 함수 호출')
    recursive_function()

  recursive_function()


#5-4. 재귀 함수 종료 예제
def ex4():

  def recursive_function(i):
    #100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
      return
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수를 종료')

  recursive_function(1)


#5-5. 2가지 방식으로 구현한 팩토리얼 예제
def ex5():
  #반복적으로 구현한 n!
  def factorial_iterative(n):
    result = 1
    #1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
      result *= i
    return result

  #재귀적으로 구현한 n!
  def factorial_recursive(n):
    if n <= 1:  #n이 1 이하인 경우 1 반환
      return 1
    #n! = n * (n-1)!를 그대로 코드로 작성
    return n * factorial_recursive(n - 1)

  print('반복적으로 구현:', factorial_iterative(5))
  print('재귀적으로 구현:', factorial_recursive(5))


#5-6. 인접 행렬 방식 예제
def ex6():
  INF = 999999999  #무한의 비용 선언

  #2차원 리스트를 이용해 인접 행렬 표현
  graph = [[0, 7, 5], [7, 0, INF], [5, INF, 0]]

  print(graph)


#5-7. 인접 리스트 방식 예제
def ex7():
  #행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
  graph = [[] for _ in range(3)]

  #노드 0에 연결된 노드 정보 저장(노드, 거리)
  graph[0].append((1, 7))
  graph[0].append((2, 5))

  #노드 1에 연결된 노드 정보 저장(노드, 거리)
  graph[1].append((0, 7))

  #노드 2에 연결된 노드 정보 저장(노드, 거리)
  graph[2].append((0, 5))

  print(graph)


#5-8. DFS 예제
def ex8():
  #DFS 메소드 정의
  def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
      if not visited[i]:  #이미 방문한 적이 없는 경우
        dfs(graph, i, visited)

  #각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
  graph = [
      [],
      [2, 3, 8],  #1번 노드는 2, 3, 8에 연결
      [1, 7],  #2번 노드
      [1, 4, 5],  #3번 노드 ...
      [3, 5],
      [3, 4],
      [7],
      [2, 6, 8],
      [1, 7]
  ]

  #각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
  visited = [False] * 9

  #정의된 DFS 함수 호출
  dfs(graph, 1, visited)


#5-9. BFS 예제
def ex9():
  from collections import deque

  #BFS 메소드 정의
  def bfs(graph, start, visited):
    #큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
      #큐에서 하나의 원소를 뽑아 출력
      v = queue.popleft()
      print(v, end=' ')
      #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
      for i in graph[v]:
        if not visited[i]:
          queue.append(i)
          visited[i] = True

  #각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
  graph = [
      [],
      [2, 3, 8],  #1번 노드는 2, 3, 8에 연결
      [1, 7],  #2번 노드
      [1, 4, 5],  #3번 노드 ...
      [3, 5],
      [3, 4],
      [7],
      [2, 6, 8],
      [1, 7]
  ]

  #각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
  visited = [False] * 9

  #정의된 BFS 함수 호출
  bfs(graph, 1, visited)

#회의실 배정 (231119)
def meetingRoom():
  n = int(input())  #회의 수
  result = 0  #회의 최대 개수

  timeArr = []
  for i in range(n):
    start, end = map(int, input().split())
    timeArr.append([start, end])
  
  timeArr.sort(key=lambda x: (x[1], x[0])) #끝나는 시간(우선), 시작 시간(차선) 기준 오름차순 정렬

  endSt = 0
  for i in range(1,n) :
    if timeArr[endSt][1] <= timeArr[i][0] :
      endSt = i
      result += 1
    
  print(result+1)

  # a = 0
  # for i in range(n):
  #   for j in range(n):
  #     if timeArr[a][1] <= timeArr[j][0] :
  #       print('확인a, j:', a, j)
  #       result += 1
  #       a = j
  #       if a == n-1 :
  #         result += 1
  
  # print(result)

  # startArr = list()
  # endArr = list()

  # for i in range(n):
  #   start, end = map(int, input().split())
  #   startArr.append(start)
  #   endArr.append(end)

  # a = 0
  # for i in range(1, n):
  #   if endArr[a] < startArr[i]:
  #     result += 1
  #     a = i
  #     if a == n - 1:
  #       result += 1

  # print(result)
def gasStation() :
  n = int(input()) #도시 개수
  d = list(map(int, input().split())) #거리 길이
  m = list(map(int, input().split())) #가격

  result = 0 #최소 비용

  minM = m[0]
  for i in range(n-1) :
    if m[i] <= minM :
      minM = m[i]
    result += d[i] * minM

  print(result)

  # m[0] * (d[0]+d[1]+d[2])
  # m[0] * d[0] + m[1] * d[1] + m[2] * d[2]
  # m[0] * d[0] + m[1] * d[1] + m[1] * d[2]

  # dcount = 0
  # a = 0
  
  # m.remove(m[n-1]) #리스트에서 마지막 m 제거
  # # print('min:',min(m))

  # for i in range(n-1) :
  #   if m[i] == min(m) :
  #     for j in range(dcount, len(d)) :
  #       # print('dcount:',dcount)
  #       # print('len(d)',len(d))
  #       a += d[j]
  #       # print('a:',a)
  #     result += a * m[i]
  #     break
  #   else :
  #     result += d[i] * m[i]
  #     # print('result:',result)
  #     dcount += 1
  #     # print('dcount:',dcount)

  # print(result)
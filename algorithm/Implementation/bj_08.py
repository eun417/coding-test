#트럭 주차 (231127~29)
def solution() :
  a, b, c = map(int, input().split()) #주차 요금
  
  time_list = [] #시간 리스트
  for _ in range(3) :
    start, end = map(int, input().split()) #도착시간, 떠난 시간
    time_list.append([start, end])
    
  time_list.sort() #시간 오름차순 정렬

  cost = 0 #주차 요금
  car_count = 0 #주차된 차의 수

  for i in range(1, 101) : #입력으로 주어지는 시간 범위 1~100 
    for time in time_list :
      if i == time[0] : #시간이 도착시간과 같다면 car_count +1
        car_count += 1
      elif i == time[1] : #시간이 떠난 시간과 같다면 car_count -1
        car_count -= 1
        
    if car_count == 1:
      cost += a*1 #주차요금 * 차 대수
    elif car_count == 2:
      cost += b*2
    elif car_count == 3:
      cost += c*3
        
  print(cost)
  

# def carCount(a, b, c, all_cost, car_count) :
#   if car_count == 1 :
#     all_cost += a
#     print('all_cost...a:', all_cost)
#   elif car_count == 2 :
#     all_cost += b
#     print('all_cost...b:', all_cost)
#   elif car_count == 3 :
#     all_cost += c
#     print('all_cost...c:', all_cost)

#   return all_cost

# def solution() :
#   a, b, c = map(int, input().split()) #1, 2, 3대 각 주차 요금
#   all_cost = 0 #총 주차 요금 = *결과값
  
#   #start, end = [] -> (X) 리스트는 따로 선언해야함
#   # start = [] 
#   # end = []
#   time_list = []
#   for _ in range(3) :
#     time = list(map(int, input().split())) #도착 시간, 떠난 시간
#     time_list.append(time)
  
#   time_list.sort() #도착시간 기준 오름차순 정렬
  
#   car_count = 0
  
#   for i in range(1, 101) :
#     for j in range(3) :
#       if i == time_list[j][0] :
#         car_count += 1
#       elif i == time_list[j][1] :
#         car_count -= 1

#       if 1 <= car_count <= 3 :
#         all_cost = carCount(a, b, c, all_cost, car_count)
    
#   print(all_cost)
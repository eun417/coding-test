#나무 조각 (231127)
def solution() :
  number_list = list(map(int, input().split())) #입력받은 수들

  while number_list != [1, 2, 3, 4, 5] :
    for j in range(1, len(number_list)) :
      if number_list[j-1] > number_list[j] :
        number_list[j-1], number_list[j] = number_list[j], number_list[j-1]
        print(*number_list)
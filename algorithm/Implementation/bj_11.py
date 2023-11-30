#트럭 (실버1) 231130
def solution() :
  n, w, l = map(int, input().split()) #트럭 수, 다리 길이, 최대하중
  a_list = list(map(int, input().split())) #트럭들의 무게

  time = 0 #모든 트럭들이 다리 건너는 최단시간 (*결과값)
  w_list = []
  
  w_sum = a_list.pop(0)
  for _ in range(n) :
    if not a_list :
      w_list.append(w_sum)
      break
    elif (w_sum+a_list[0]) <= l :
      w_sum += a_list.pop(0)
      time += 1
    else :
      w_list.append(w_sum)
      w_sum = a_list.pop(0)

  time += w*len(w_list)+1
  
  print(time)
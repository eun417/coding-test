#위에서 아래로 (내 코드)
#삽입 정렬 사용
def solution() :
  n = int(input())  #수열에 속해 있는 수의 개수
  
  num_list = list()  #수열
  for i in range(n) :
    num_list.append(int(input()))  #입력받은 수를 리스트에 삽입

  for i in range(1, n):
    for j in range(i, 0, -1):
      if num_list[j] > num_list[j - 1]:
        num_list[j], num_list[j - 1] = num_list[j - 1], num_list[j]
        
  print(*num_list)
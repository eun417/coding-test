#수 정렬하기 (브론즈2) 231214 🅾
def solution() :
  #0. 정렬 라이브러리
  n = int(input())  #수의 개수
  data_list = []  #수열
  for _ in range(n) :
    data = int(input())  #수 입력
    data_list.append(data)
  
  data_list.sort()  #정렬
  
  #결과 출력
  for i in range(n) :
    print(data_list[i])
  
  # #1. 선택 정렬
  # n = int(input())  
  # data_list = []
  # for _ in range(n) :
  #   data = int(input())  
  #   data_list.append(data)

  # for i in range(n) :
  #   min_index = i  #가장 작은 수의 인덱스
  #   for j in range(i+1, n) :
  #     #min_index의 값보다 작은 값이 있다면
  #     if data_list[min_index] > data_list[j] :  
  #       min_index = j  #min_index를 j로 변경
  #   #min_index의 값과 i의 값을 바꿈
  #   data_list[i], data_list[min_index] = data_list[min_index], data_list[i]

  # #결과 출력
  # for i in range(n) :
  #   print(data_list[i])

  # #2. 삽입 정렬
  # n = int(input())
  # data_list = []
  # for i in range(n) :
  #   data = int(input())
  #   data_list.append(data)

  # for i in range(n) :
  #   for j in range(i, 0, -1) :  #인덱스 i부터 1까지 감소하며 반복
  #     if data_list[j] < data_list[j-1] :
  #       data_list[j], data_list[j-1] = data_list[j-1], data_list[j]
  #     else :
  #       break  #자기보다 작은 데이터 만나면 멈춤

  # for i in range(n) :
  #   print(data_list[i])

  # #3. 퀵 정렬
  # n = int(input())
  # data_list = []
  # for i in range(n) :
  #   data = int(input())
  #   data_list.append(data)

  # def quick_sort(array) :
  #   #리스트가 하나 이하의 원소만 담고 있다면 종료
  #   if len(array) <= 1:
  #     return array

  #   pivot = array[0]  #피벗은 첫 번째 원소
  #   tail = array[1:]  #피벗을 제외한 리스트

  #   left_side = [x for x in tail if x <= pivot]  #분할된 왼쪽 부분
  #   right_side = [x for x in tail if x > pivot]  #분할된 오른쪽 부분

  #   #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행, 전체 리스트 반환
  #   return quick_sort(left_side) + [pivot] + quick_sort(right_side)

  # for i in range(n) :
  #   print(quick_sort(data_list)[i])

  # #5. 계수 정렬
  # #모든 원소의 값이 0보다 크거나 같다고 가정
  # n = int(input())
  # data_list = []
  # for i in range(n) :
  #   data = int(input())
  #   data_list.append(data)

  # #모든 범위를 포함하는 리스트 선언(0으로 초기화)
  # count = [0] * (max(data_list) + 1)

  # for i in range(n) :
  #   count[data_list[i]] += 1  #각 데이터에 해당하는 인덱스의 값 증가

  # for i in range(len(count)) :
  #   for j in range(count[i]) :
  #     print(i)
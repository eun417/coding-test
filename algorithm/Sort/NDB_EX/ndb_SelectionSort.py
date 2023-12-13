#선택 정렬
#가장 작은 것을 선택 -> 맨 앞 데이터와 교환 
#-> 그다음 작은 데이터 선택 -> 앞에서 두 번째 데이터와 교환 ...

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i  #가장 작은 원소의 인덱스
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]  #스와프
print(array)


#파이썬 스와프
array = [3, 5]
array[0], array[1] = array[1], array[0]

print(array)
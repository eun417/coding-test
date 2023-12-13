#두 배열의 원소 교체 (내 코드)
def solution():
  n, k = map(int, input().split())  #원소 개수, 바꿔치기 횟수

  a_list = list(map(int, input().split()))
  b_list = list(map(int, input().split()))

  a_list.sort()
  b_list.sort(reverse=True)  #내림차순 정렬

  for i in range(k):
    if a_list[i] < b_list[i]:
      a_list[i], b_list[i] = b_list[i], a_list[i]

  print(sum(a_list))
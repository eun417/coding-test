#소트인사이드 (실버5) 231214 🅾
def solution() :
n = list(input())  #정렬할 수

for i in range(len(n)) :
  n[i] = int(n[i])  #문자 -> 정수 변환

n.sort(reverse=True)  #내림차순 정렬

#결과 출력
for i in range(len(n)) :
  print(n[i], end='')
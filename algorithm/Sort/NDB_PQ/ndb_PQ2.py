#성적이 낮은 순서로 학생 출력 (내 코드)
def solution() :
  n = int(input())  #학생 수
  student_list = []
  for i in range(n) :
    a, b = input().split()  #이름, 점수
    student_list.append((a, int(b)))

  student_list.sort(key = lambda x : x[1])  #점수를 기준으로 리스트 오름차순 정렬

  for i in student_list:
    print(i[0], end=' ')
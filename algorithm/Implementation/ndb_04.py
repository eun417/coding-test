#문자열 재정렬 (231122)
def solution():
  s = input()  #문자열(알파벳 대문자, 숫자0~9)
  als = []  #알파벳
  ns = []  #숫자

  for i in range(len(s)):
    if s[i].isalpha():
      als.append(s[i])  #알파벳이면 als에 추가
    else:
      ns.append(s[i])  #나머지는 ns에 추가

  als.sort()  #알파벳 정렬

  sum = 0
  for i in range(len(ns)):
    sum += int(ns[i])  #숫자들 합

  if sum != 0:
    als.append(sum)  #als 리스트에 sum도 추가

  for i in range(len(als)):
    print(als[i], end='')  #als 전체 출력

# 2309번 일곱 난쟁이 (브론즈1) 240114 - 완전탐색
def solution() :
  from itertools import combinations
  
  n = []  #아홉 난쟁이 키 리스트
  for _ in range(9) :
    n.append(int(input()))

  #combinations()로 조합 구함
  for tall in combinations(n, 7) :
    if sum(tall) == 100 :
      n = sorted(tall)
      break

  for i in range(len(n)) :
    print(n[i])
# 22864: 피로도 (브론즈2) 240130 🅾 
# - 수학/구현/그리디/사칙연산/시뮬레이션
def solution() :
  a, b, c, m = map(int, input().split())
  work = 0
  fatigue = 0
  
  for _ in range(24) :
    if fatigue + a <= m :
      work += b
      fatigue += a
    elif fatigue + a > m :
      fatigue -= c
      if fatigue < 0 :
        fatigue = 0

  print(work)
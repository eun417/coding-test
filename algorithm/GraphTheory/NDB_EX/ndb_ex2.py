# 10-2. 경로 압축 기법
def find_parent2(parent, x):
  if parent[x] != x:
    parent[x] = find_parent2(parent, parent[x])
  return parent[x]
def coinZero():
  n, k = map(int, input().split())

  result = 0

  a = []
  for i in range(n):
    a.append(int(input()))

  for i in range(n-1, -1, -1):
    if a[i] <= k:
      result += k // a[i]
      k %= a[i]

  print(result)

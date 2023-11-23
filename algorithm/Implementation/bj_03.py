#바구니 뒤집기 (231123)
def solution():
  n, m = map(int, input().split())

  #처음엔 바구니에 적힌 번호와 같은 번호 공 들어있음
  basket_list = []
  for i in range(1, n + 1):
    basket_list.append(i)
  # print(basket_list)

  for _ in range(m):
    i, j = map(int, input().split())
    tmp = basket_list[i-1:j]
    tmp.reverse()
    basket_list[i-1:j] = tmp

  print(*basket_list)

  #
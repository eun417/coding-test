#공 바꾸기 (231123)
def solution() :
  n, m = map(int, input().split()) #n: 바구니, m: 행
  basket_list = []

  #처음엔 바구니에 적힌 번호와 같은 번호 공 들어있음
  for i in range(1, n+1) : 
    basket_list.append(i) 

  # print(basket_list)
  
  for a in range(m) :
    i, j = map(int, input().split()) #입력받은 바구니 번호
    tmp = basket_list[i-1]
    basket_list[i-1] = basket_list[j-1]
    basket_list[j-1] = tmp
    
  print(*basket_list)
  #
#바구니 순서 바꾸기 - 브론즈2 (231127)
def solution() :
  n, m = map(int, input().split()) #n:바구니 개수, m:회전 횟수
  
  arr = [] #바구니 순서
  for i in range(n) : 
    arr.append(i+1) #1~n 번호 부여

  # print(arr)
  
  for _ in range(m) :
    i, j, k = map(int,input().split()) #i~j번째 바구니, k:기준 바구니
    i, j, k = i-1, j-1, k-1 #시작점 0
    tmp = []
    for a in range(i, j+1) :
      if k == j+1 :
        for b in reversed(range(len(tmp))) :
          arr.remove(tmp[b])
          arr.insert(i, tmp[b])
      else :
        tmp.append(arr[k])
        # print('k:',k)
        k += 1
      
      # if k == j+1 :
      #   for b in range(len(tmp)) :
      #     arr[a] = tmp[b]
      #     a += 1
      #     print(arr)
      #   break
      # else :
      #   tmp.append(arr[a])
      #   print('tmp:', tmp)
      #   arr[a] = arr[k]
      #   print('k:', k)
      #   print('a:', a)
      #   k += 1

  print(*arr)
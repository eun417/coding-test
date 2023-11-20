def lostBracket() :
  n = input().split('-') #'-' 기준으로 문자열 나눔
  result = 0
  
  a = list(map(int, n[0].split('+'))) #'-' 이전 문자열(식)을 '+' 기준으로 나눔
  result += sum(a) 
  
  for i in range(1, len(n)) : #'-' 기준으로 나눈 요소들을 반복문으로 처리
    a = list(map(int, n[i].split('+'))) #'-'로 나눈 요소 안에 있는 식을 '+' 기준으로 나눔
    result -= sum(a)
  
  print(result)
  
  # a=''
  
  # for i in range(len(n)) :
  #   if n[i] == '+' :
  #     result += int(a)
  #     a=''
  #   elif n[i] == '-' :
  #     result -= int(a)
  #     a=''
  #   else :
  #     a += n[i]
  #     n[i-1] = a
  #     print('n[i-1]:',n[i-1])

  # print(len(n))
  # for i in range(len(n)) :
  #   print(n[i], end=' ')
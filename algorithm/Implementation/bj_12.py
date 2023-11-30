#킹 (실버3) 231130
def solution() :
  k, s, n = input().split() #킹 위치, 돌 위치, 움직이는 횟수

  dx = [0, 0, -1, 1, 1, 1, -1, -1] #R, L, B, T / RT, LT, RB, LB
  dy = [1, -1, 0, 0, 1, -1, 1, -1]
  
  kx = int(k[1]) #킹의 x좌표
  ky = ord(k[0])-64 #킹의 y좌표

  # print('kx:', kx, end=' ')
  # print('ky:', ky)
  # print('k:', k)

  sx = int(s[1]) #돌의 x좌표
  sy = ord(s[0])-64 #킹의 y좌표

  # print('sx:', sx, end=' ')
  # print('sy:', sy)
  # print('s:', s)

  for _ in range(int(n)) :
    move = input() #움직이는 정보
    tmp = [kx, ky, sx, sy] #좌표 임시저장
    # print('tmp:', tmp)

    if move == 'R' :
      kx += dx[0]
      ky += dy[0]
      # print('kx:',kx)      
      # print('ky:',ky)

      #킹과 돌의 좌표가 동일한 경우 돌 이동
      if kx == sx and ky == sy :
        sx += dx[0]
        sy += dy[0]
        # print('sx:',sx)      
        # print('sy:',sy)

    elif move == 'L' :
      kx += dx[1]
      ky += dy[1]
      # print('kx:',kx)      
      # print('ky:',ky)

      if kx == sx and ky == sy :
        sx += dx[1]
        sy += dy[1]
        # print('sx:',sx)      
        # print('sy:',sy)
        
    elif move == 'B' :
      kx += dx[2]
      ky += dy[2]
      # print('kx:',kx)      
      # print('ky:',ky)

      if kx == sx and ky == sy :
        sx += dx[2]
        sy += dy[2]
        # print('sx:',sx)      
        # print('sy:',sy)
        
    elif move == 'T' :
      kx += dx[3]
      ky += dy[3]
      # print('kx:',kx)      
      # print('ky:',ky)

      if kx == sx and ky == sy :
        sx += dx[3]
        sy += dy[3]
        # print('sx:',sx)   
        # print('sy:',sy)

    elif move == 'RT' : 
      kx += dx[4]
      ky += dy[4]
      # print('kx:',kx)      
      # print('ky:',ky)

      if kx == sx and ky == sy :
        sx += dx[4]
        sy += dy[4]
        # print('sx:',sx)      
        # print('sy:',sy)

    elif move == 'LT' : 
      kx += dx[5]
      ky += dy[5]
      # print('kx:',kx)      
      # print('ky:',ky)

      if kx == sx and ky == sy :
        sx += dx[5]
        sy += dy[5]
        # print('sx:',sx)      
        # print('sy:',sy)

    elif move == 'RB' : 
      kx += dx[6]
      ky += dy[6]
      # print('kx:',kx)      
      # print('ky:',ky)

      if kx == sx and ky == sy :
        sx += dx[6]
        sy += dy[6]
        # print('sx:',sx)      
        # print('sy:',sy)

    elif move == 'LB' : 
      kx += dx[7]
      ky += dy[7]
      # print('kx:',kx)      
      # print('ky:',ky)

      if kx == sx and ky == sy :
        sx += dx[7]
        sy += dy[7]
        # print('sx:',sx)   
        # print('sy:',sy)

    #체스판을 벗어날 경우 임시저장한 좌표들 다시 대입
    if kx < 1 or kx > 8 or ky < 1 or ky > 8 or sx < 1 or sx > 8 or sy < 1 or sy > 8 :
      kx = tmp[0]
      ky = tmp[1]
      sx = tmp[2]
      sy = tmp[3]

    #체스판 안에 해당하는 좌표만 나옴
    k = chr(ky+64)+str(kx)
    s = chr(sy+64)+str(sx)
      
  print(k)
  print(s)
    
  # board[kx][ky] = 1

  # # 체스판 출력
  # for i in range(len(board)) :
  #   for j in range(len(board)) :
  #     print(board[i][j], end=' ')
  #   print()

  # for _ in range(int(n)) :
  #   move = input() #움직이는 정보

  #   if move == 'R' :
  #     kx = kx + dx[0]
  #     ky = ky + dy[0]
  #     print('kx:',kx)      
  #     print('ky:',ky)

  #     if (kx == sx and ky == sy) and 0<sy<7  :
  #       sy += 1
  #       print('sx:',sx)      
  #       print('sy:',sy)
  
  #   elif move == 'L' :
  #     kx = kx + dx[1]
  #     ky = ky + dy[1]
  #     print('kx:',kx)      
  #     print('ky:',ky)

  #     if (kx == sx and ky == sy) and 0<sy<7 :
  #       sy -= 1
  #       print('sx:',sx)      
  #       print('sy:',sy)
  
  #   elif move == 'B' :
  #     kx = kx + dx[2]
  #     ky = ky + dy[2]
  #     print('kx:',kx)      
  #     print('ky:',ky)

  #     if (kx == sx and ky == sy) and 0<sx<7 :
  #       sx += 1
  #       print('sx:',sx)      
  #       print('sy:',sy)

  #   elif move == 'T' :
  #     kx = kx + dx[3]
  #     ky = ky + dy[3]
  #     print('kx:',kx)      
  #     print('ky:',ky)

  #     if (kx == sx and ky == sy) and 0<sx<7 :
  #       sx -= 1
  #       print('sx:',sx)      
  #       print('sy:',sy)

  #   elif move == 'RT' :
  #     kx = kx + dx[4]
  #     ky = ky + dy[4]
  #     print('kx:',kx)      
  #     print('ky:',ky)

  #     if (kx == sx and ky == sy) and 0<sx<7 and 0<sy<7 :
  #       sx -= 1
  #       sy += 1
  #       print('sx:',sx)      
  #       print('sy:',sy)
 
  #   elif move == 'LT' :
  #     kx = kx + dx[5]
  #     ky = ky + dy[5]
  #     print('kx:',kx)      
  #     print('ky:',ky)

  #     if (kx == sx and ky == sy) and 0<sx<7 and 0<sy<7 :
  #       sx -= 1
  #       sy -= 1
  #       print('sx:',sx)      
  #       print('sy:',sy)

  #   elif move == 'RB' :
  #     kx = kx + dx[6]
  #     ky = ky + dy[6]
  #     print('kx:',kx)      
  #     print('ky:',ky)

  #     if (kx == sx and ky == sy) and 0<sx<7 and 0<sy<7 :
  #       sx += 1
  #       sy += 1
  #       print('sx:',sx)      
  #       print('sy:',sy)

  #   elif move == 'LB' :
  #     kx = kx + dx[7]
  #     ky = ky + dy[7]
  #     print('kx:',kx)      
  #     print('ky:',ky)

  #     if (kx == sx and ky == sy) and 0<sx<7 and 0<sy<7 :
  #       sx += 1
  #       sy -= 1
  #       print('sx:',sx)      
  #       print('sy:',sy)

  #   if 0 <= (8-kx) < 8 and 0 <= ky < 8 :
  #     k = chr(ky+65)+str(8-kx)

  #   if 0 <= (8-sx) < 8 and 0 <= sy < 8 :
  #     s = chr(sy+65)+str(8-sx)

  # print('*k:', k)
  # print('*s:', s)
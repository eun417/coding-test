#럭키 스트레이트 (231122)
def solution() :
  n = input() #점수
  ln, rn = [], []

  for i in range(1, len(n)+1) :
    if i == (len(n) // 2) :
      ln = n[:i] #왼쪽 부분
      rn = n[i:] #오른쪽 부분
      # print('ln:', ln)
      # print('len(ln):', len(ln))
      # print('rn:', rn)

  ln_sum = 0
  rn_sum = 0
  for i in range(len(ln)) :
    ln_sum += int(ln[i])
    rn_sum += int(rn[i])
    # print('ln_sum:', ln_sum)
    # print('rn_sum:', rn_sum)

  if ln_sum == rn_sum :
    print('LUCKY')
  else :
    print('READY')
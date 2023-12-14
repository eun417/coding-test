#단어 정렬 (실버5) 231214 🅾
def solution() :
  n = int(input())  #단어의 개수

  words = set()  #중복 제거 위해 set 선언
  for i in range(n) :
    words.add(input())

  words = list(words)  #set -> list 변환
  for i in range(len(words)) :
    words[i] = list(words[i])  #단어 -> 리스트 변환(한 글자씩 분리)

  words.sort(key = lambda x : (len(x), x))  #길이순, 같으면 사전순 정렬

  #결과 출력
  for i in words :
    for j in range(len(i)) :
      print(i[j], end='')
    print()
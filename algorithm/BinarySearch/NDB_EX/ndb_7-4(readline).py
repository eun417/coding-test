#7-4. 한 줄 입력받아 출력
#readline() : 빠르게 입력받음
#readline()으로 입력하면 엔터가 줄 바꿈 기호로 입력
#-> 공백문자 제거 위해 rstrip() 사용
import sys
#하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

#입력받은 문자열 그대로 출력
print(input_data)
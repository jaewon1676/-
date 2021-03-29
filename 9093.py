# 백준 9093 단어 뒤집기
import sys
input = sys.stdin.readline

n = int(input()) # 입력 할 숫자 입력
data = [list(input().split()) for i in range(n)] 
# 문자 입력 하고 list형으로 data변수에 저장한다.
for i in range(n):
    for j in data[i]: # data 변수의 문자를 j 변수에 옮긴다
        print(''.join(reversed(list(j))), end=" ")
        # join 함수를 이용해 받은 문자를 더해 문자열로 연결하고
        # reversed 함수를 이용해 문자열을 뒤집는다.
    print()
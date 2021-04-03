# 백준 17413 단어 뒤집기2

import sys
input = sys.stdin.readline

s = list(input().strip())
reverse = True         # 문자열을 뒤집을 지 판단
answer = ''            # 전체 문자열을 저장
word = ''              # 일부 문자열을 저장

for i in s:
    if i == '<':            # <가 뜨면 단어를 뒤집지 못하게 한다.
        reverse = False
        answer += word
        word = '<'
    
    elif i == '>':          # >
        reverse = True
        answer += (word + '>')
        word = ''
    
    elif i == ' ':          # 공백
        answer += (word + ' ')
        word = ''
    
    elif reverse == True:   # reverse == True이면
        word = i + word     # i값을 먼저 저장하고 뒤에 word 값을 저장해
                            # 문자열을 뒤집어준다.
    else:                   # 규칙이 잘 지켜지면 문자를 word에 추가
        word += i

print(answer + word)
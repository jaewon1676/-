# 백준 2744 대소문자 바꾸기
word = list(str(input())) # 여러개의 문자열을 리스트구조로 저장한다.
answer = [] 

for character in word:
    if character in 'abcdefghijklmnopqrstuvwxyz': # 소문자인경우 대문자로 바꾸어줌
        answer.append(character.upper())
    else:                                         # 대문자인경우 소문자로 바꾸어줌
        answer.append(character.lower())
for character in answer:
    print(character, end = '') # character변수 끝까지 출력

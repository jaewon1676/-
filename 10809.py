# 백준 10809 알파벳 찾기

word = input()
alphabet = list(range(97,123)) # 아스키코드 숫자 범위

for i in alphabet:
    print(word.find(chr(i)))
    # chr함수를 사용해 숫자를 문자형으로 변환
    # 문자 -> 숫자로 변환할 때는 ord함수 사용
    # find 함수는 문자열에서만 사용 가능.
    # index함수를 사용해 리스트, 튜플도 가능
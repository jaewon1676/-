# 백준 1157 단어 공부
# 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
words = input().upper() # 문자열 입력 받고 대문자 변환
unique_words = list(set(words)) # set함수로 중복 제거

cnt_list = []
for x in unique_words:
    cnt = words.count(x) # words 변수의 문자열 개수를 cnt 변수에 저장
    cnt_list.append(cnt) # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1: # count 숫자 최대값이 중복되면
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])
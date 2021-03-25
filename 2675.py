# 백준 2675 문자열 반복
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해서
# 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
t = int(input())   # 테스트 케이스의 개수를 받는다.
for i in range(t): # t만큼 반복
    r, s = input().split() #반복횟수 r, 문자열 S를 입력 받는다.
    text = ''     # 문자열을 출력할 공간
    for i in s:
        text += int(r) * i # 반복횟수만큼 i를 text변수에 넣는다.
    print(text)




# 백준 5355 화성수학
# @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다.
case = int(input()) # case 개수를 받는다.

for _ in range(case): # 받은 case 개수만큼 돌린다.
    mars = list(map(str, input().split())) # mars 변수에 list 구조, str 형식으로 저장한다.
    answer = 0                 # 결과를 구할 변수
    for i in range(len(mars)): # mars 변수 길이만큼 돌린다.
        if i == 0:
            answer += float(mars[i])
        else:
            if mars[i] == "#":
                answer -= 7
            elif mars[i] == "%":
                answer += 5
            elif mars[i] == "@":
                answer *= 3
                
    print("%0.2f" % answer)
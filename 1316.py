# 백준 1316 그룹 단어 체커
n=int(input())
answer=0

for i in range(n):
    word = input() # 단어 입력
    for j in range(len(word)): # 단어 길이만큼 검사
        if j != len(word) - 1:
            if word[j] == word[j + 1]:
                pass # pass는 그냥 넘어간다는 뜻
            elif word[j] in word[j + 1:]:
                break
        else:
            answer+=1
print(answer)

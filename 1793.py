# 백준 1793 타일링
# DP
# 테스트케이스가 주어지지 않아 try & except 구문 사용
import sys
input = sys.stdin.readline
p = [0 for _ in range(251)] # 입력 n <= 250
while(True):
    try:    # n에 아무것도 입력 받지 않으면 break.           
        n = int(input())
        p[0] = 1
        p[1] = 1
        p[2] = 3
        # p = [1, 1, 3]으로도 선언 가능
        for i in range(3, 251): # or (3, n+1) 
            p[i] = p[i-1] + (p[i-2]*2)
            # 251까지 p[i]를 정의 해 놓는다.
        print(p[n])
    except:
        break
# try:
#     실행할 코드
# except:
#     예외가 발생했을 때 처리하는 코드
# 백준 2751 수 정렬하기 2
# 오름차순 정렬 
import sys
input = sys.stdin.readline
# input을 통해 입력 받을 시 sys.stdin.readline으로 입력 받도록 바꾼다.
n = int(input())                        # 수를 입력받을 개수
nums = [int(input()) for _ in range(n)] # n번 입력 받아 nums에 저장.
nums.sort()                             # 오름차순 정렬
print(*nums)                            # *을 사용해 리스트 해제
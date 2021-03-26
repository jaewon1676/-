# 2750 백준 수 정렬하기
# n개의 수를 입력 받아 오름차순으로 정렬 한다.
import sys
input = sys.stdin.readline

n = int(input())                        # 수를 입력받을 개수
nums = [int(input()) for _ in range(n)] # n번 입력받아 nums에 저장
nums.sort()                             # 오름차순 정렬
print(*nums)                            # 리스트 해제 후 출력
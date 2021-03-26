# 백준 11931 수 정렬하기 4
import sys
input = sys.stdin.readline
# input을 통해 입력 받을 시 sys.stdin.readline으로 입력 받도록 바꾼다.
n = int(input())                        # 수를 입력받을 개수
nums = [int(input()) for _ in range(n)] # n번 입력 받아 nums에 저장.
nums.sort(reverse=True)                 # 내림차순 정렬
print(*nums)                            # *을 사용해 리스트 해제


#-------------------------------한줄코드
#print(*sorted([int(sys.stdin.readline()) for _ in range(int(input()))], reverse=True))
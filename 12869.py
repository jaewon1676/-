# 백준 12869 뮤탈리스크
# DP
#첫 번째로 공격받는 SCV는 체력 9를 잃는다.
#두 번째로 공격받는 SCV는 체력 3을 잃는다.
#세 번째로 공격받는 SCV는 체력 1을 잃는다.
import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
m.sort() # 오름차순 정렬

# 1, 3, 2 순서대로 공격을 하면, 남은 체력은 
# (12-9, 10-1, 4-3) = (3, 9, 1)이다. 
# 2, 1, 3 순서대로 공격을 하면, 남은 체력은 (0, 0, 0)이다.
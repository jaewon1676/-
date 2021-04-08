# 백준 2108 통계학
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)] 

nums.sort()
top_num = Counter(nums).most_common()

print("%.f"%(sum(nums)/N))   # 산술평균
print(nums[N//2])            # 중앙값
if len(nums) > 1:            # 최빈값 
    if top_num[0][1] == top_num[1][1]:
        print(top_num[1][0]) 
    else: 
        print(top_num[0][0]) 
else: 
    print(nums[0]) 
    
print(nums[-1] - nums[0])    # 범위
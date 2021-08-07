# 듣보잡

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list_n = [input().strip() for i in range(n)]
list_m = [input().strip() for i in range(m)]

duplicate = list(set(list_n) & set(list_m))

print(len(duplicate))
for i in sorted(duplicate):
    print(i)
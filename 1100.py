# 하얀 칸

arr = []
for _ in range(8):
    arr.append(list(map(str, input())))

cnt = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: # 하얀칸
            if arr[i][j] == 'F': # F일경우
                cnt += 1

print(cnt)
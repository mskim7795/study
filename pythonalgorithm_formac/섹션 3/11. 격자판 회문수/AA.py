import sys
# sys.stdin = open("input.txt", "r")

arr = [list(map(int, input().split())) for _ in range(7)]
res = 0

for i in range(7):
    for j in range(2, 5):
        for k in range(1, 3):
            if arr[i][j-k] != arr[i][j+k]:
                break
        else:
            res += 1
        for k in range(1, 3):
            if arr[j-k][i] != arr[j+k][i]:
                break
        else:
            res += 1

print(res)
import sys
# sys.stdin = open("input.txt", "r")

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

maxV = -2147000000
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += arr[i][j]
    maxV = max(tmp, maxV)

for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += arr[j][i]
    maxV = max(tmp, maxV)

tmp = 0
for i in range(n):
    tmp += arr[i][i]
maxV = max(tmp, maxV)

tmp = 0
for i in range(n):
    tmp += arr[i][n-i-1]
maxV = max(tmp, maxV)

print(maxV)

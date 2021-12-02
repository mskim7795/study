import sys
# sys.stdin = open("input.txt", "r")

n = int(input())

arr = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
res = 0

for i in range(1, n + 1):
    arr[i][1:n + 1] = list(map(int, input().split()))
    
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] > arr[i][j - 1] and arr[i][j] > arr[i][j + 1] and arr[i][j] > arr[i - 1][j] and arr[i][j] > arr[i + 1][j]:
            res += 1

print(res)
import sys
# sys.stdin = open("input.txt", "r")

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    row, drct, num = map(int, input().split())

    for j in range(num):
        for k in range(n - 1):
            if drct == 0:
                arr[row - 1][k - 1], arr[row - 1][k] = arr[row - 1][k], arr[row - 1][k - 1]
            else:
                arr[row - 1][n - 1 - k], arr[row - 1][n - 2 - k] = arr[row - 1][n - 2 - k], arr[row - 1][n - 1 - k]

s = 0
e = n
sumV = 0

for i in range(n):
    for j in range(s, e):
        sumV += arr[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sumV)
import sys
# sys.stdin = open("input.txt", "r")

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
sumV = 0

for i in range(n):
    for j in range(abs(n // 2 - i), n - abs(n // 2 - i)):
        sumV += arr[i][j]

print(sumV)
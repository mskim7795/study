import sys
from collections import deque
# sys.stdin = open("input.txt", "r")


n = int(input())

arr = list(list(map(int, input().split())) for _ in range(n))

s = e = n // 2
sumV = 0
for i in range(n // 2 + 1):
    for j in range(s, e + 1):
        sumV += arr[i][j]
    s -= 1
    e += 1

s += 2
e -= 2
for i in range(n // 2 + 1, n):
    for j in range(s, e + 1):
        sumV += arr[i][j]
    s += 1
    e -= 1

print(sumV)
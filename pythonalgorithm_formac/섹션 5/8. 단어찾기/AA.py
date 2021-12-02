import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n = int(input())
arr1 = []
arr2 = []
res = ""
for _ in range(n):
    arr1.append(input())
for _ in range(n-1):
    arr2.append(input())
arr1.sort()
arr2.sort()

while arr2:
    tmp1 = arr1.pop()
    tmp2 = arr2.pop()
    if tmp1 != tmp2:
        res = tmp1
        break
else:
    res = arr1.pop()

print(res)
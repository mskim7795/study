import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

if n <= m:
    for _ in range(n):
        arr2.append(arr1.pop())
    arr2.sort()
    for i in range(n+m):
        print(arr2[i], end=' ')
else:
    for _ in range(m):
        arr1.append(arr2.pop())
    arr1.sort()
    for i in range(n + m):
        print(arr1[i], end=' ')









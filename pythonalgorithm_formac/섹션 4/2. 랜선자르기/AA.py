import sys
# sys.stdin = open("input.txt", "r")

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

lt = 1
rt = -2147000000
mid = 0
res = 0
for i in arr:
    rt = max(i, rt)
while lt <= rt:
    mid = (lt + rt) // 2
    tmp = 0
    for i in arr:
        tmp += i // mid
    if tmp >= n:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1

print(res)
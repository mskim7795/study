import sys
# sys.stdin = open("input.txt", "r")

n, c = map(int, input().split())
arr = list(int(input()) for _ in range(n))

arr.sort()
lt = arr[0]
rt = arr[n-1]
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 1
    horse = arr[0]
    maxV = 21470000
    for x in arr:
        dis = x - horse
        if dis >= mid:
            horse = x
            cnt += 1
            maxV = min(maxV, dis)
    if cnt < c:
        rt = mid - 1
    else:
        res = max(res, maxV)
        lt = mid + 1

print(res)
import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

lt = 1
rt = sum(arr)
mid = 0
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 1
    tmp = 0
    for i in range(n):
        tmp += arr[i]
        if tmp > mid:
            cnt += 1
            tmp = arr[i]
    if cnt <= m:
        rt = mid - 1
        res = mid
    else:
        lt = mid + 1

print(res)
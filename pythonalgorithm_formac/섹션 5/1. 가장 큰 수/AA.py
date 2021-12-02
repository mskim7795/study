import sys
# sys.stdin = open("input.txt", "r")

arr, m = map(int, input().split())
arr = str(arr)
num = []
res = []
for x in arr:
    num.append(int(x))
cnt = 0
i = 0
while cnt < m and i < len(num):
    if len(res) == 0:
        res.append(num[i])
        i += 1
    else:
        tmp = res.pop()
        if num[i] <= tmp:
            res.append(tmp)
            res.append(num[i])
            i += 1
        else:
            cnt += 1
while i < len(num):
    res.append(num[i])
    i += 1
if len(res) > len(num) - m:
    for _ in range(len(res) -len(num) + m):
        res.pop()
for x in res:
    print(x, end="")
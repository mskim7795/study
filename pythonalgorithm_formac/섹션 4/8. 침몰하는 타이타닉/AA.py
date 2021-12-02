import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

arr.sort(reverse=True)
check = [0]*n
i = 0
for i in range(n):
    if check[i] == 1:
        continue
    sumV = 0
    num = 0
    for j in range(i, n):
        if check[j] == 1:
            continue
        else:
            if sumV + arr[j] <= m:
                sumV += arr[j]
                check[j] = 1
                num += 1
            else:
                continue
        if num == 2:
            break
    cnt += 1
print(cnt)
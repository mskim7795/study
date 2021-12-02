import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sumArr = [[0 for _ in range(n)] for _ in range(n)]
count = 0
for i in range(n):
    sumArr[i][i] = arr[i]

j = 0
for i in range(n):
    for j in range(i, n):
        if i == j:
            tmp = sumArr[i][i]
        else:
            sumArr[i][j] = sumArr[i][j-1] + sumArr[j][j]
            tmp = sumArr[i][j]
        if tmp < m:
            continue
        if tmp == m:
            count += 1
            break
        if tmp > m:
            break
    else:
        break


print(count)










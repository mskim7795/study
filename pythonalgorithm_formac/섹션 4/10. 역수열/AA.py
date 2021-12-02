import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
res = [0]*n
for i in range(n):
    cnt = arr[i]
    for j in range(n):
        if res[j] == 0:
            if cnt == 0:
                res[j] = i + 1
                break
            else:
                cnt -= 1

for x in res:
    print(x, end=" ")
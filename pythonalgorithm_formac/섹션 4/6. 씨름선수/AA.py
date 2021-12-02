import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
hum = [list(map(int, input().split())) for _ in range(n)]
hum.sort(reverse=True)

res = list()
for h1, w1 in hum:
    for h2, w2 in res:
        if h2 > h1 and w2 > w1:
            break
    else:
        res.append([h1, w1])

print(len(res))
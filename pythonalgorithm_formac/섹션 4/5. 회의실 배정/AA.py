import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x: (x[1], x[0]))
res = list()
res.append(meet[0])
cnt = 1
for i in range(1, n):
    pop = res.pop()
    res.append(pop)
    if meet[i][0] >= pop[1]:
        res.append(meet[i])
        cnt += 1

print(cnt)

import sys
# sys.stdin = open("input.txt", "r")


def dfs(num, minV):
    global cnt
    if num > m:
        for i in range(m):
            print(res[i], end=" ")
        print()
        cnt += 1
    else:
        for i in range(minV, n + 1):
            res.append(i)
            dfs(num + 1, i + 1)
            res.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(range(1, n + 1))
    res = []
    cnt = 0
    dfs(1, 1)
    print(cnt)



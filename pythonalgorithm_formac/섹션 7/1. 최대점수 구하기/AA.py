import sys
# sys.stdin = open("input.txt", "r")


def dfs(tm, pnt, idx):
    global maxV
    if tm > m:
        return
    else:
        maxV = max(pnt, maxV)
        for i in range(idx, n):
            if ch[i] == 0:
                ch[i] = 1
                dfs(tm + arr[i][1], pnt + arr[i][0], i + 1)
                ch[i] = 0



if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(tuple(map(int, input().split())) for _ in range(n))
    arr.sort(key=lambda x: x[1]/x[0])
    ch = [0] * n
    maxV = 0
    dfs(0, 0, 0)
    print(maxV)

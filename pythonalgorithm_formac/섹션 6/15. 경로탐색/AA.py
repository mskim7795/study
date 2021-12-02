import sys
# sys.stdin = open("input.txt", "r")


def dfs(pnt, cnt):
    global res
    if cnt >= n:
        return
    elif pnt == n:
        res += 1
        return
    else:
        for i in range(1, n + 1):
            if inj[pnt][i] == 1 and ch[i] == 0:
                ch[i] = 1
                dfs(i, cnt + 1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(m))
    inj = list([0] * (n+1) for _ in range(n+1))
    for s, e in arr:
        inj[s][e] = 1
    res = 0
    ch = [0] * (n+1)
    ch[1] = 1
    dfs(1, 0)

    print(res)

import sys
# sys.stdin = open("input.txt", "r")


def dfs(idx, bowl):
    global res
    if idx == n:
        if 0 < bowl <= sumV:
            if ch[bowl] == 0:
                ch[bowl] = 1
                res += 1
                return
    else:
        dfs(idx + 1, bowl + arr[idx])
        dfs(idx + 1, bowl - arr[idx])
        dfs(idx + 1, bowl)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    sumV = sum(arr)
    ch = [0] * (sumV + 1)
    res = 0
    dfs(0, 0)

    print(sumV - res)


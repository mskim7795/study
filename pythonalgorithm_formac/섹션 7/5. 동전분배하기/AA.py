import sys
# sys.stdin = open("input.txt", "r")


def dfs(a, b, c, idx):
    global res
    if idx == n:
        tmp = max(a, b, c) - min(a, b, c)
        if tmp < res and a != b and b != c and c != a:
            res = tmp
    else:
        dfs(a + arr[idx], b, c, idx + 1)
        dfs(a, b + arr[idx], c, idx + 1)
        dfs(a, b, c + arr[idx], idx + 1)



if __name__ == "__main__":
    n = int(input())
    arr = list(int(input()) for _ in range(n))
    res = 2147000000
    dfs(0, 0, 0, 0)
    print(res)







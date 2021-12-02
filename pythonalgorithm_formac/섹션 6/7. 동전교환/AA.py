import sys
# sys.stdin = open("input.txt", "r")


def D(x, c):
    global minV, coin
    if x > res or c > minV:
        return
    elif x == res:
        minV = min(c, minV)
        return
    else:
        for i in range(n):
            D(x + coin[i], c + 1)


if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    coin.sort(reverse=True)
    res = int(input())
    minV = 2147000000
    D(0, 0)
    print(minV)


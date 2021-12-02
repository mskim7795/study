import sys
# sys.stdin = open("input.txt", "r")


def F(x):
    global res
    tmp = [0]
    if len(x) == 2:
        res = x[1]
        return
    for i in range(1, len(x) - 1):
        tmp.append(x[i] + x[i+1])
    F(tmp)

def D(L):
    global res
    if L > n:
        F(arr)
        if res == f:
            for i in range(1, n + 1):
                print(arr[i], end=" ")
            sys.exit(0)
        else:
            res = 0
            return
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                arr[L] = i
                D(L + 1)
                ch[i] = 0
                arr[L] = 0

if __name__ == "__main__":
    n, f = map(int, input().split())
    arr = [0] * (n + 1)
    ch = [0] * (n + 1)
    res = 0
    D(1)



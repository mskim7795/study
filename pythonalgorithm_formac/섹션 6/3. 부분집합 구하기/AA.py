import sys
# sys.stdin = open("input.txt", "r")
n = 0
def DFS(x, res):
    if x > n + 1:
        return
    else:
        DFS(x + 1, res + str(x) + " ")
        DFS(x + 1, res)
        if x == n+1:
            print(res)


if __name__ == "__main__":
    n = int(input())
    DFS(1, "")



import sys
# sys.stdin = open("input.txt", "r")

arr = [list(map(int, input().split())) for _ in range(9)]
def isStoku():
    for i in range(9):
        for j in range(8):
            for k in range(j + 1, 9):
                if arr[i][j] == arr[i][k]:
                    return False
                if arr[j][i] == arr[k][i]:
                    return False
                if arr[(i // 3) * 3 + j // 3][(((i % 3) * 3) % 9) + j % 3] == arr[(i // 3) * 3 + k // 3][(((i % 3) * 3) % 9) + k % 3]:
                    return False
    return True

res = isStoku()
if res:
    print('YES')
else:
    print('NO')
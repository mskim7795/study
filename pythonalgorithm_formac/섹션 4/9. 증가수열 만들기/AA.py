import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))

maxV = 0
lt = 0
rt = n-1
str = str()
while lt < rt:
    if maxV < arr[lt] < arr[rt]:
        maxV = arr[lt]
        lt += 1
        str += "L"
    elif maxV < arr[rt] < arr[lt]:
        maxV = arr[rt]
        rt -= 1
        str += "R"
    elif arr[lt] < maxV < arr[rt]:
        maxV = arr[rt]
        rt -= 1
        str += "R"
    elif arr[rt] < maxV < arr[lt]:
        maxV = arr[lt]
        lt += 1
        str += "L"
    else:
        break
print(len(str))
print(str)

import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))


def digit_sum(x):
    summ = 0
    while True:
        summ += x%10
        x //= 10
        if x == 0:
            return summ

maxNum = -2147000000
res = 0

for x in arr:
    tmp = digit_sum(x)
    if tmp > maxNum:
        maxNum = tmp
        res = x

print(res)
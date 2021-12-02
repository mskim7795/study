import sys
#sys.stdin=open("input.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum+=arr[i]
avg = round(sum / n)

minRes = abs(avg - arr[0])
resNum = 0
for i in range(1, n):
    if abs(avg - arr[i]) <= minRes and arr[i] != arr[resNum]:
        minRes = abs(avg - arr[i])
        if arr[i] > arr[minRes]:
            resNum = i
print("%d %d" %(avg, resNum + 1))

import sys
# sys.stdin=open("input.txt", "r")

n = int(input())

arr = list(map(int, input().split()))
point = 0
con = 0
for i in range(n):
    if arr[i] == 0:
        con = 0
    elif arr[i] == 1:
        con +=1
        point += con

print(point)





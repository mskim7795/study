import sys
# sys.stdin=open("input.txt", "r")

n = int(input())

for i in range(n):
    check = True
    str = input().upper()
    for j in range(len(str)//2):
        if str[j] != str[len(str)-1-j]:
            print('#%d NO' %(i+1))
            check = False
            break
    if check:
        print('#%d YES' %(i+1))







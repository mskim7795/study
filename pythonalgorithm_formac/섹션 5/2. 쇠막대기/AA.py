import sys
# sys.stdin = open("input.txt", "r")

stick = str(input())
cnt = 0
sumV = 0
bef = ""
for x in stick:
    if x == "(":
        cnt += 1
    elif x == ")":
        cnt += -1
        if bef == "(":
            sumV += cnt
        elif bef == ")":
            sumV += 1
    bef = x

print(sumV)
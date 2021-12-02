import sys
# sys.stdin = open("input.txt", "r")
string = input()
res = []
for x in string:
    if x.isdecimal():
        res.append(int(x))
    else:
        v2 = res.pop()
        v1 = res.pop()
        if x == "+":
            res.append(v1 + v2)
        elif x == "-":
            res.append(v1 - v2)
        elif x == "*":
            res.append(v1 * v2)
        else:
            res.append(v1 / v2)
print(res.pop())
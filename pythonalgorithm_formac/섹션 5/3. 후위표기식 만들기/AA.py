import sys
# sys.stdin = open("input.txt", "r")

inp = str(input())
arr = []
oper = []
for x in inp:
    arr.append(x)
for x in arr:
    if x.isdecimal():
        print(x, end="")
    elif len(oper) == 0:
        oper.append(x)
    elif x == ")":
        while True:
            tmp = oper.pop()
            if tmp == "(":
                break
            print(tmp, end="")
    elif x == "*" or x == "/":
        tmp = oper.pop()
        if tmp == "*" or tmp == "/":
            print(tmp, end="")
            oper.append(x)
        else:
            oper.append(tmp)
            oper.append(x)
    elif x == "+" or x == "-":
        while len(oper) > 0:
            tmp = oper.pop()
            if tmp == "(":
                oper.append(tmp)
                break
            else:
                print(tmp, end="")
        oper.append(x)
    else:
        oper.append(x)
while len(oper) > 0:
    tmp = oper.pop()
    print(tmp, end="")
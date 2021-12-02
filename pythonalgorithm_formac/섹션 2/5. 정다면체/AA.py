import sys
#sys.stdin=open("input.txt", "rt")
n, m = map(int, input().split())
diceN = list(range(1, n+1))
diceM = list(range(1, m+1))
sumDict = {}
minNum = 0
res = []

for dN in diceN:
    for dM in diceM:
        tmp = dN + dM
        if sumDict.get(tmp) == None:
            sumDict[tmp] = 1
        else:
            sumDict[tmp]+=1

for key, val in sumDict.items():
    if val > minNum:
        minNum = val
        res.clear()
        res.append(key)
    elif val == minNum:
        res.append(key)

for x in res:
    print(x, end=" ")




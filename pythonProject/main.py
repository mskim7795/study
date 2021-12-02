import requests

def start(prob):
    response = requests.post("https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod/start",
                             headers={'X-Auth-Token': 'b0ca2319a472fafe25b85b5d174e56c9', 'Content-Type': 'application/json'}
                             , json={'problem': prob})
    return response.json()

def waitingLine(auth):
    response = requests.get("https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod/waiting_line",
                            headers={'Authorization': auth, 'Content-Type': 'application/json'})
    response = response.json()
    response = response["waiting_line"]
    ret = []
    for x in response:
        ret.append([x['id'], x['from']])
    ret.sort(key=lambda y: y[1])

    return ret

def gameResult(auth):
    response = requests.get("https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod/game_result",
                            headers={'Authorization': auth, 'Content-Type': 'application/json'}).json()
    return response['game_result']

def userInfo(auth):
    response = requests.get("https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod/user_info",
                            headers={'Authorization': auth, 'Content-Type': 'application/json'}).json()
    response = response['user_info']
    ret = {}
    for x in response:
        ret[x['id']] = x['grade']
    return ret

def match(auth, pairs):
    response = requests.put("https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod/match",
                            headers={'Authorization': auth, 'Content-Type': 'application/json'},
                            json={'pairs': pairs})
    return response.json()

def changeGrade(auth, commands):
    response = requests.put("https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod/change_grade",
                            headers={'Authorization': auth, 'Content-Type': 'application/json'},
                            json={'commands': commands})
    return response.json()

def score(auth):
    response = requests.get("https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod/score",
                            headers={'Authorization': auth, 'Content-Type': 'application/json'})
    return response.json()

if __name__ == "__main__":
    problem = 1
    s = start(problem)
    auth = s['auth_key']
    users = userInfo(auth)
    changes = []

    time = 0

    for i in range(1, len(users) + 1):
        changes.append({'id': i, 'grade': 4000})
    changeGrade(auth, changes)

    for i in range(596):        # matching
        matchs = []
        waitUsers = waitingLine(auth)
        usersInfo = userInfo(auth)
        gameResults = gameResult(auth)
        ch = [0] * (len(waitUsers))

        for g in gameResults:   # give a point
            w = g['win']
            l = g['lose']
            t = g['taken']
            if problem == 2 and t <= 10:
                continue
            usersInfo[w] += 1000 - int(t / 40 * 1000)
            usersInfo[l] -= 1000 - int(t / 40 * 1000)

        changes = []
        for i in range(1, len(usersInfo) + 1):
            changes.append({'id': i, 'grade': usersInfo[i]})
        changeGrade(auth, changes)

        for j in range(len(waitUsers)):         # find pairs
            if ch[j] == 0:
                for k in range(j + 1, len(waitUsers)):
                    if ch[k] == 0:
                        if abs(usersInfo[waitUsers[j][0]] - usersInfo[waitUsers[k][0]]) <= 200 + 400 * (time - waitUsers[j][1]):
                            ch[j] = ch[k] = 1
                            matchs.append([waitUsers[j][0], waitUsers[k][0]])
                            break
        time = match(auth, matchs)['time']



        print(time)
        print(waitUsers)
        print(usersInfo)
        print()

    point = score(auth)
    print(point)


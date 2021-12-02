import requests

def start(problem):
    headers = {"X-Auth-Token": "13512b09d82eeabb9439d50eccae9665"}
    data = {"problem": problem}
    return requests.post("https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users/start", headers=headers, json=data)

def locations(auth):
    headers = {"Authorization": auth}
    return requests.get("https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users/locations", headers=headers)

def trucks(auth):
    headers = {"Authorization": auth}
    return requests.get("https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users/trucks", headers=headers)

def simulate(auth, commands):
    headers = {"Authorization": auth}
    return requests.put("https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users/simulate", headers=headers, json=commands)

def score(auth):
    headers = {"Authorization": auth}
    return requests.get("https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users/score", headers=headers)

def move():


if __name__ == '__main__':
    auth = start(1).json()['auth_key']
    locs = {}
    trus = {}
    lenl = len(locations(auth).json()['locations'])
    lent = len(trucks(auth).json()['trucks'])
    chTck = [0] * lent
    for i in range(720):

        for j in range(lent):
            if chTck[j] != 0:
                chTck[j] -= 1

        loc = locations(auth).json()['locations']
        sumV = 0
        lacks = []
        overs = []
        for x in loc:
            locs[x['id']] = x['located_bikes_count']
            sumV += locs[x['id']]
        avg = sumV // len(loc)

        for k, v in locs.items():
            if v <= avg // 2:
                lacks.append(k)
            elif v >= avg * 3 // 2:
                overs.append(k)


        tck = trucks(auth).json()['trucks']
        for x in tck:
            trus[x['id']] = [x['location_id'], x['loaded_bikes_count']]


        for lack in lacks:
            for over in overs:

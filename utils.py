import json

def loadClubs():
    with open('clubs.json') as c:
        return json.load(c)['clubs']

def loadCompetitions():
    with open('competitions.json') as comps:
        return json.load(comps)['competitions']

def updateCompetitionPoints(competition):
    with open('competitions.json', 'r') as file:
        all_datas = json.load(file)
        for comp in all_datas['competitions']:

            if comp['name'] == competition['name']:
                comp['numberOfPlaces'] = competition['numberOfPlaces']

        with open('competitions.json', 'w') as file:
            json.dump(all_datas, file, indent=4)

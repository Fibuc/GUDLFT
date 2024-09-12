import json
from datetime import datetime

def load_clubs():
    with open('clubs.json') as c:
        return json.load(c)['clubs']


def load_competitions():
    with open('competitions.json') as comps:
        return json.load(comps)['competitions']


def _update_json_file(name_file, element_to_update):
    if name_file == 'competitions':
        key_to_update = 'numberOfPlaces'

    elif name_file == 'clubs':
        key_to_update = 'points'

    with open(f'{name_file}.json', 'r') as file:
        all_datas = json.load(file)
        for element in all_datas[name_file]:

            if element['name'] == element_to_update['name']:
                element[key_to_update] = element_to_update[key_to_update]

        with open(f'{name_file}.json', 'w') as file:
            json.dump(all_datas, file, indent=4)


def update_points_and_places(competition, club):
    _update_json_file('competitions', competition)
    _update_json_file('clubs', club)
    

def has_event_passed(value: str):
    event_date = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    return event_date < datetime.now()


def get_usable_points(competition, club):
    points = 12
    if club['points'] < points:
        points = club['points']

    if competition['numberOfPlaces'] < points:
        points = competition['numberOfPlaces']
    
    return points
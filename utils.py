import json
from datetime import datetime
from pathlib import Path

COMPETITION_JSON_FILE = Path(__file__).parent / 'competitions.json'
CLUB_JSON_FILE = Path(__file__).parent / 'clubs.json'

def load_clubs():
    return _load_json(CLUB_JSON_FILE)['clubs']


def load_competitions():
    return _load_json(COMPETITION_JSON_FILE)['competitions']


def _load_json(file_name):
    with open(file_name) as file:
        return json.load(file)


def save_json(file_name, datas):
    with open(file_name, 'w') as file:
        json.dump(datas, file, indent=4)


def update_points_and_places(competitions, clubs):
    competitions_datas = _load_json(COMPETITION_JSON_FILE)
    competitions_datas['competitions'] = competitions
    save_json(COMPETITION_JSON_FILE, competitions_datas)

    clubs_datas = _load_json(CLUB_JSON_FILE)
    clubs_datas['clubs'] = clubs
    save_json(CLUB_JSON_FILE, clubs_datas)


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

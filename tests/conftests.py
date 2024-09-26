import pytest
from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def get_club_datas(low_points: bool=False):
    club_datas = [{'name': 'Club test', 'email': 'club@example.com', 'points': 15}]
    if low_points:
        club_datas[0]['points'] = 1

    return club_datas


def get_competition_datas(option: str=''):
    competition_datas = [{
        'name': 'Competition test', 'date': '2050-11-22 13:30:00',
        'numberOfPlaces': 16, 'clubs': {}
    }]
    if option == 'past':
        competition_datas[0]['date'] = '2021-11-22 13:30:00'

    elif option == 'places':
        competition_datas[0]['numberOfPlaces'] = 1

    elif option == 'history':
        competition_datas[0]['clubs'] = {'Club test': 11}
    
    return competition_datas


@pytest.fixture
def data_post():
    return {
        'competition': 'Competition test',
        'club': 'Club test',
        'places': 1
    }

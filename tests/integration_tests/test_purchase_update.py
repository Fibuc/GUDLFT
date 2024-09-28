from unittest.mock import patch
from tests.conftests import client, get_club_datas, get_competition_datas, data_post
import server
import utils


class TestPurchaseUpdate:

    def setup_method(self, method):
        server.clubs = get_club_datas()
        server.competitions = get_competition_datas()
        self.club_email = server.clubs[0]['email']

    def test_purchase_update_points(self, client, data_post):
        with patch('server.update_points_and_places') as mock_update:
            club, competition = server.clubs[0], server.competitions[0]
            initial_club_points = club['points']
            initial_competitions_places = competition['numberOfPlaces']
            requested_places = data_post['places']
            purchase_response = client.post('/purchasePlaces', data=data_post, follow_redirects=True)
            assert purchase_response.status_code == 200
            assert server.clubs[0]['points'] == initial_club_points - requested_places
            assert server.competitions[0]['numberOfPlaces'] == initial_competitions_places - requested_places
            assert club['name'] in competition['clubs']
            assert requested_places == competition['clubs'][club['name']]

from unittest.mock import patch

from tests.conftests import (
    client, get_club_datas, get_competition_datas, data_post
)
import server


class TestPurchasePlaces:

    # Setup of the default configuration for each test in the class
    def setup_method(self, method):
        server.clubs = get_club_datas()
        server.competitions = get_competition_datas()

    # Happy path
    def test_purchase_success(self, client, data_post):
        with patch('server.update_points_and_places') as mock_update:
            response = client.post(
                '/purchasePlaces', data=data_post,
                follow_redirects=True
            )
            assert response.status_code == 200

    # Sad path
    def test_purchase_not_enough_club_points(self, client, data_post):
        server.clubs = get_club_datas(low_points=True)
        data_post['places'] = 12
        response = client.post('/purchasePlaces', data=data_post)
        assert response.status_code == 400

    def test_purchase_more_than_12_places(self, client, data_post):
        data_post['places'] = 13
        response = client.post('/purchasePlaces', data=data_post)
        assert response.status_code == 400

    def test_purchase_event_already_passed(self, client, data_post):
        server.competitions = get_competition_datas(option='past')
        response = client.post('/purchasePlaces', data=data_post)
        assert response.status_code == 400

    def test_purchase_with_negative_number(self, client, data_post):
        data_post['places'] = -4
        response = client.post('/purchasePlaces', data=data_post)
        assert response.status_code == 400

    def test_purchase_with_string(self, client, data_post):
        data_post['places'] = 'abc'
        response = client.post('/purchasePlaces', data=data_post)
        assert response.status_code == 400

    def test_purchase_overbooking(self, client, data_post):
        data_post['places'] = 8
        server.competitions = get_competition_datas(option='places')
        response = client.post('/purchasePlaces', data=data_post)
        assert response.status_code == 400

    def test_purchase_overbooking_with_multiple_reservations(
            self, client, data_post
    ):
        data_post['places'] = 5
        server.competitions = get_competition_datas(option='history')
        response = client.post('/purchasePlaces', data=data_post)
        assert response.status_code == 400

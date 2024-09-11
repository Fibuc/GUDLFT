from tests.conftests import client
from unittest.mock import patch

MOCK_CLUB = [{
    'name':'Club test',
    'email':'club@example.com',
    'points':'8'
}]

MOCK_COMPETITION = [{
    'name': 'Competition test',
    'date': '2024-10-22 13:30:00',
    'numberOfPlaces': '7'
}]

class TestShowSummary:

    def test_show_summary_valid_email(self, client):
        with patch('server.clubs', MOCK_CLUB):
            response = client.post(
                '/showSummary',
                data={'email': 'club@example.com'}
            )
            assert response.status_code == 200
            assert b'club@example.com' in response.data

    def test_show_summary_invalid_email(self, client):
        with patch('server.clubs', MOCK_CLUB):
            response = client.post(
                '/showSummary',
                data={'email': 'invalid@example.com'}
            )
            assert response.status_code == 400
            assert b'Invalid email address' in response.data

    def test_show_summary_empty_email(self, client):
        with patch('server.clubs', MOCK_CLUB):
            response = client.post(
                '/showSummary',
                data={'email': ''}
            )
            assert response.status_code == 400
            assert b'The email address cannot be empty' in response.data
    
    def test_show_summary_without_authentication(self, client):
        with patch('server.clubs', MOCK_CLUB):
            response = client.get('/showSummary')
            assert response.status_code == 405


class TestPurchasePlaces:

    def test_purchase_success(self, client):
        initial_places = int(MOCK_COMPETITION[0]['numberOfPlaces'])
        places_booked = 5
        with patch('server.clubs', MOCK_CLUB), patch('server.competitions', MOCK_COMPETITION):
            response = client.post(
                '/purchasePlaces',
                data={
                    'competition': 'Competition test',
                    'club': 'Club test',
                    'places': str(places_booked)
                }
            )
            assert response.status_code == 200
            assert b'Great-booking complete!' in response.data
            expected_places = initial_places - places_booked
            assert int(MOCK_COMPETITION[0]['numberOfPlaces']) == expected_places

    @patch('server.clubs', MOCK_CLUB)
    @patch('server.competitions', MOCK_COMPETITION)
    def test_purchase_not_enough_club_points(self, client):
        response = client.post(
            '/purchasePlaces',
            data={
                'competition': 'Competition test',
                'club': 'Club test',
                'places': '12'
            }
        )
        assert response.status_code == 400
        assert b'You do not have enough points to book that many places.' in response.data

    @patch('server.clubs', [{
        'name':'Club test','email':'club@example.com','points':'20'
    }])
    @patch('server.competitions', [{
    'name': 'Competition test', 'date': '2020-10-22 13:30:00',
    'numberOfPlaces': '20'
    }])
    def test_purchase_more_than_12_places(self, client):
        response = client.post(
            '/purchasePlaces',
            data={
                'competition': 'Competition test',
                'club': 'Club test',
                'places': '15'
            }
        )
        assert response.status_code == 400
        assert b'You cannot book more than 12 places per competition.' in response.data

    @patch('server.clubs', MOCK_CLUB)
    @patch('server.competitions', [{
    'name': 'Competition test', 'date': '2020-10-22 13:30:00',
    'numberOfPlaces': '20'
    }])
    def test_purchase_event_already_passed(self, client):
        response = client.post(
            '/purchasePlaces',
            data={
                'competition': 'Competition test',
                'club': 'Club test',
                'places': '5'
            }
        )
        assert response.status_code == 400
        assert b'You cannot book places for an event that has already passed.' in response.data

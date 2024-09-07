from tests.conftests import client
from unittest.mock import patch

MOCK_CLUB = [{
    'name':'Club test',
    'email':'club@example.com',
    'points':'8'
}]

MOCK_COMPETITION = [{
    'name': 'Competition test',
    'date': '2020-10-22 13:30:00',
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
        with patch('server.clubs', MOCK_CLUB), patch('server.competitions', MOCK_COMPETITION):
            response = client.post(
                '/purchasePlaces',
                data={
                    'competition': 'Competition test',
                    'club': 'Club test',
                    'places': '5'
                }
            )
            assert response.status_code == 200
            assert b'Great-booking complete!' in response.data

    def test_purchase_not_enough_club_points(self, client):
        with patch('server.clubs', MOCK_CLUB), patch('server.competitions', MOCK_COMPETITION):
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

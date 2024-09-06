from tests.conftests import client
from unittest.mock import patch

MOCK_CLUB = [{
    'name':'Club test',
    'email':'club@example.com',
    'points':'8'
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

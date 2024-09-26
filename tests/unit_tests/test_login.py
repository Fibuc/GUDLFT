from tests.conftests import client, get_club_datas, get_competition_datas
import server


class TestShowSummary:
    
    # Setup of the default configuration for each test in the class
    def setup_method(self, method):
        server.clubs = get_club_datas()
        server.competitions = get_competition_datas()

    # Happy path test
    def test_show_summary_valid_email(self, client):
        response = client.post(
            '/showSummary', data={'email': 'club@example.com'}
        )
        assert response.status_code == 200
        assert b'club@example.com' in response.data

    # Sad path tests
    def test_show_summary_invalid_email(self, client):
        response = client.post(
            '/showSummary', data={'email': 'invalid@example.com'}
        )
        assert response.status_code == 400

    def test_show_summary_empty_email(self, client):
        response = client.post('/showSummary', data={'email': ''})
        assert response.status_code == 400
    
    def test_show_summary_without_authentication(self, client):
        response = client.get('/showSummary')
        assert response.status_code == 405

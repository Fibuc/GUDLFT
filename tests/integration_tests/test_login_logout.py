from tests.conftests import client, get_club_datas, get_competition_datas
import server


class TestLoginLogout:

    def setup_method(self, method):
        server.clubs = get_club_datas()
        server.competitions = get_competition_datas()

    def test_login_logout(self, client):
        club_email = server.clubs[0]['email']
        login_response = client.post(
            '/showSummary', data={'email': club_email}
        )
        logout_response = client.get('/logout')
        assert login_response.status_code == 200
        assert logout_response.status_code == 302

from unittest.mock import patch

from tests.conftests import (
    client, get_club_datas, get_competition_datas, data_post
)
import server


class TestLoginPurchase:

    def setup_method(self, method):
        server.clubs = get_club_datas()
        server.competitions = get_competition_datas()
        self.club_email = server.clubs[0]['email']

    def test_login_purchase(self, client, data_post):
        with patch('server.update_points_and_places') as mock_update:
            login_response = client.post(
                '/showSummary', data={'email': self.club_email}
            )
            assert login_response.status_code == 200

            purchase_response = client.post(
                '/purchasePlaces', data=data_post, follow_redirects=True
            )
            assert purchase_response.status_code == 200

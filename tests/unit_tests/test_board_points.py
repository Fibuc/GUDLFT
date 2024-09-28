from tests.conftests import client

class TestPointsClubBoard:

    def test_get_club_points_board(self, client):
        response = client.get('/clubPointsBoard')
        assert response.status_code == 200

    def test_post_club_points_board(self, client):
        response = client.post('/clubPointsBoard')
        assert response.status_code == 405
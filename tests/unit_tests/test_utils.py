from tests.conftests import get_competition_datas, get_club_datas
import utils


class TestLoadElements:

    def test_load_clubs(self):
        clubs = utils.load_clubs()
        assert clubs is not None
        assert isinstance(clubs, list)
        assert isinstance(clubs[0], dict)

    def test_load_competitions(self):
        competitions = utils.load_competitions()
        assert competitions is not None
        assert isinstance(competitions, list)
        assert isinstance(competitions[0], dict)


class TestCompetitionDate:

    # Happy path
    def test_past_competition_date(self):
        competition_date = get_competition_datas('past')[0]['date']
        competion_already_past = utils.has_event_passed(competition_date)
        assert competion_already_past is True

    # Sad path
    def test_future_competition_date(self):
        competition_date = get_competition_datas()[0]['date']
        competion_already_past = utils.has_event_passed(competition_date)
        assert competion_already_past is False


class TestGetUsablePoints:

    def test_usable_points_are_club_points(self):
        club = get_club_datas(low_points=True)[0]
        competition = get_competition_datas()[0]
        expected_points = club['points']
        points = utils.get_usable_points(competition, club)
        assert points == expected_points

    def test_usable_points_are_competition_points(self):
        club = get_club_datas()[0]
        competition = get_competition_datas('places')[0]
        expected_points = competition['numberOfPlaces']
        points = utils.get_usable_points(competition, club)
        assert points == expected_points

    def test_usable_points_are_12_points(self):
        club = get_club_datas()[0]
        competition = get_competition_datas()[0]
        expected_points = 12
        points = utils.get_usable_points(competition, club)
        assert points == expected_points

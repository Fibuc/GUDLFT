from pathlib import Path

from locust import HttpUser, task, between

from utils import load_clubs, load_competitions, save_json, CLUB_JSON_FILE, COMPETITION_JSON_FILE


class ProjectPerfTest(HttpUser):
    host = 'http://127.0.0.1:5000'
    wait_time = between(1, 2)
    club = load_clubs()[0]
    competition = load_competitions()[0]
    max_execution_purchase = 1
    current_execution_purchase = 0

    def on_start(self):
        self.clubs = load_clubs()
        self.competitions = load_competitions()

    def on_stop(self):
        save_json(CLUB_JSON_FILE, datas={'clubs': self.clubs})
        save_json(COMPETITION_JSON_FILE, datas={'competitions': self.competitions})

    @task
    def index(self):
        self.client.get('')

    @task
    def login(self):
        self.client.post('/showSummary', {'email': self.club['email']})
        
    @task
    def logout(self):
        self.client.get('/logout')

    @task
    def club_points_board(self):
        self.client.get('/clubPointsBoard')

    @task
    def book(self):
        self.client.get(f'/book/{self.competition['name']}/{self.club['name']}')

    @task
    def purchase(self):
        if self.current_execution_purchase < self.max_execution_purchase:
            self.client.post('/purchasePlaces', data={
                'competition': self.competition['name'],
                'club': self.club['name'],
                'places': 1
            })
            self.current_execution_purchase += 1
        
        else:
            self.stop(True)

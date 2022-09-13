from locust import HttpUser, task
from test_data import inputs

class WebsiteTestUser(HttpUser):

    @task
    def get_home_page(self):
        self.client.get("/")

    @task
    def make_prediction(self):
        self.client.post("/predict", json=inputs)
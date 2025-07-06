from locust import HttpUser, task, between
import random

CITIES = ["New York", "London", "Tokyo", "Sydney", "Delhi"]

class FastAPIUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def load_home(self):
        self.client.get("/")

    @task(3)
    def load_weather(self):
        city = random.choice(CITIES)
        self.client.get(f"/weather/{city}")

    @task(2)
    def load_weather_card(self):
        city = random.choice(CITIES)
        self.client.get(f"/weather-card/{city}")

from locust import HttpUser, task, between
import random

class MyBot(HttpUser):
    wait_time = between(0.1, 0.2) 

    @task
    def attack_fastapi(self):
        fake_name = f"Bot_User_{random.randint(1, 100000)}"
        self.client.get(f"/?name={fake_name}")
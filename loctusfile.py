from locust import HttpUser, task, between
import random 
class MyBot(HttpUser):
    wait_time = between(0.5, 1.0)
    @task(1)
    def load_main_page(self):
        self.client.get("/")

    @task(3)
    def fill_form(self):
        bot_number = random.randint(1000, 99999)
        fake_name = f"Bot_Number_{bot_number}"
        self.client.post("/submit", data= {
            "name": fake_name,
            "eamil": f"bot{bot_number}@hacker.com"
        })
from locust import HttpUser, task, between

class MyAppUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def home_page(self):
        self.client.get("/")

    @task
    def api_call(self):
        self.client.get("/api/health")

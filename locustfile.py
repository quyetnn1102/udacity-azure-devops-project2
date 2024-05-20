from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    data = {"CHAS": {"0": 0}, "RM": {"0": 6.575}, "TAX": {"0": 296.0}, "PTRATIO": {"0": 15.3}, "B": {"0": 396.9},
            "LSTAT": {"0": 4.98}}
    @task(1)
    def test1(self):
        self.client.get("https://quyetnn-udacity-project2.azurewebsites.net/")

    @task(2)
    def test2(self):
        self.client.post("https://quyetnn-udacity-project2.azurewebsites.net:443/predict", json=self.data)
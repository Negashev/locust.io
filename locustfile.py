import os
from locust import HttpLocust, TaskSet, task

url = os.getenv("URL")


class UserBehavior(TaskSet):
    @task
    def index(self):
        self.client.get(url)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = os.getenv("MIN_WAIT")
    max_wait = os.getenv("MAX_WAIT")
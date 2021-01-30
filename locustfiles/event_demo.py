from locust import HttpUser, events, between,task


'''5、事件event，在负载测试的开始或结束时运行'''


class demo1(HttpUser):
    wait_time = between(2, 3)

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")
        print("hello_world")


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("A new test is starting")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("A new test is ending")




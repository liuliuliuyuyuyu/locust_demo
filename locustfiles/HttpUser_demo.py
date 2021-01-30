from locust import HttpUser, constant, task
from locust.exception import RescheduleTask

'''6、HttpUser类，包含client属性是HttpSession实例，HttpSession是requests.session的子类，所以可以保持会话一致'''


class test_httpUser(HttpUser):
    wait_time = constant(2)

    @task
    def test_demo1(self):
        data = 'username=hrptest&password=e10adc3949ba59abbe56e057f20f883e&context=ygt&businessOfficeId=3509020101' \
               '&businessTime=2021-01-26& '
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/87.0.4280.88 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        response = self.client.post("/api/login", data=data, headers=headers)
        print("Response status code:", response.status_code)
        print("Response text:", response.text)


'''7、手动控制请求的成功和失败，这咯使用with as，并且请求参数中需要增加catch_response=True'''


class test_httpUser_Hand(HttpUser):
    wait_time = constant(2)

    @task
    def test_demo1(self):
        data = 'username=hrptest&password=e10adc3949ba59abbe56e057f20f883e&context=ygt&businessOfficeId=3509020101' \
               '&businessTime=2021-01-26& '
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/87.0.4280.88 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        with self.client.post("/api/login", data=data, headers=headers, catch_response=True) as response:
            if response.status_code == 404:
                raise RescheduleTask()
            elif response.status_code == 200:
                response.success()
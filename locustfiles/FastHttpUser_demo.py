# -*- coding: utf-8 -*-

from locust import task, between
from locust.contrib.fasthttp import FastHttpUser


class MyUser(FastHttpUser):  # 继承FastHttpUser，提高性能
    wait_time = between(2, 3)
    connection_timeout = 60.0  # 连接超时时间
    max_retries = 1  # 最大重试次数，默认为 1，表示不重试
    network_timeout = 60.0  # 网络超时时间

    @task  # 使用task标记任务
    def demo1(self):
        response1 = self.client.get("/hello")  # 发送FastHttpSession请求，获取FastResponse响应
        response2 = self.client.get("/world")
        print("hello_world")

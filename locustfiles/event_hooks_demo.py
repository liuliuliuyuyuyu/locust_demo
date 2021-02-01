# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     event_hooks_demo
   Description :
   Author :        yuhua
   date：          2021/2/1
-------------------------------------------------
"""
__author__ = 'yuhua'

from locust import events, HttpUser, between, task


class demo1(HttpUser):
    wait_time = between(2, 3)

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")
        print("hello_world")


@events.request_success.add_listener  # 设置请求成功时的操作
def my_success_handler(request_type, name, response_time, response_length, **kw):
    print("Successfully made a request to: %s" % name)


@events.request_failure.add_listener  # 设置请求错误时的操作
def my_failure_handler(request_type, name, response_time, response_length, **kw):
    print("failure made a request to: %s" % name)


@events.init.add_listener  # 设置一个扩展的地址，下面的函数访问host/added_page会得到"Another page"的响应
def on_locust_init(web_ui, **kw):
    @web_ui.app.route("/added_page")
    def my_added_page():
        return "Another page"

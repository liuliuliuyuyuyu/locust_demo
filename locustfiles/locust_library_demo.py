# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     locust_library_demo
   Description :
   Author :        yuhua
   date：          2021/2/1
-------------------------------------------------
"""
__author__ = 'yuhua'

import gevent
from locust import HttpUser, task, between
from locust.env import Environment
from locust.stats import stats_printer, stats_history
from locust.log import setup_logging

'''设置logging等级'''
setup_logging("INFO", None)


'''负载脚本'''
class User(HttpUser):
    wait_time = between(1, 3)
    host = "https://docs.locust.io"

    @task
    def my_task(self):
        self.client.get("/")
        print('get_success')

    @task
    def task_404(self):
        self.client.get("/non-existing-path")
        print('get_non-existing-path')


'''setup Environment and Runner 设置环境和Runner，环境中的参数为用户类的类名'''
env = Environment(user_classes=[User])
env.create_local_runner()


'''start a WebUI instance 开启Web UI 用于查看统计信息并控制运行程序'''
env.create_web_ui("127.0.0.1", 8089)


'''start a greenlet that periodically outputs the current stats 开启一个携程定期地输出当前统计数据'''
gevent.spawn(stats_printer(env.stats))


'''start a greenlet that save current stats to history 开启一个携程保存当前统计数据到数据历史中'''
gevent.spawn(stats_history, env.runner)


'''start the test 开启测试'''
env.runner.start(1, spawn_rate=10)


'''in 60 seconds stop the runner 60s后停止测试'''
gevent.spawn_later(30, lambda: env.runner.quit())


'''wait for the greenlets 等待上面协程结束'''
env.runner.greenlet.join()


'''stop the web server for good measures 停止Web UI'''
env.web_ui.stop()

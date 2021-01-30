import time

from locust import HttpUser, task, between

'''
1、first demo
继承HttpUser类，这个类是users的子类，有很多方法和变量已经定义好可以用了，具体可以看一下users类
用户根据权重调用一个方法运行，运行后会根据等待时间进行睡眠，睡眠结束后会重新根据权重调用一个新任务执行，并循环重复
执行代码locust -f locust_files/my_locust_file.py，文件夹/文件名
'''


# 它继承自HttpUser，该属性为每个用户提供了一个 client 属性，该属性是HttpSession的一个实例。可用于向负载测试的目标系统发出 HTTP 请求
# 当您开始测试运行时，Locust将为每个并发用户创建该类的实例，并且每个虚拟用户会在自己的 gevent 线程中运行这些实例。
class demo1(HttpUser):
    weight = 1
    wait_time = between(2, 3)  # 模拟用户思考时间

    @task  # 通过用 @task 装饰方法来声明任务,只有通过 @task 装饰的方法才会在 Locust 虚拟用户运行过程中被调用
    def hello_world(self):
        """
        在类中定义host或者web页面定义host，下面的get请求会合并到host发送
        例如host=http://localhost:8089,则这个get就是会发送到http://localhost:8089/hello
        所以下面的get要排除host部分，只要path
        """
        self.client.get("/hello")
        self.client.get("/world")

    @task(3)  # 当虚拟用户运行时，会从两个任务中选择一个运行，由于 view_item 的权重为 3，因此在选择任务时会有三倍的机会选择 view_item
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)

    def on_start(self):  # 每个虚拟用户启动时调用
        self.client.post("/login", json={"username": "foo", "password": "bar"})
        print('on_start')

    def on_stop(self):  # 每个虚拟用户结束时调用
        print('on_stop')


'''2、 weight test'''


class test_weight1(HttpUser):
    # 测试weight
    weight = 3

    def on_start(self):
        self.client.get("/test_weight1111")
        print('test_weight1111')


class test_weight2(HttpUser):
    # 测试weight
    weight = 1

    def on_start(self):
        self.client.get("/test_weight2222")
        print('test_weight2222')

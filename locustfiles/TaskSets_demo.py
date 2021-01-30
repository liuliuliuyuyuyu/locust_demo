from locust import User, TaskSet, constant, task, SequentialTaskSet

'''1、 使用tasks = {}调用，并且赋予权重'''


class ForumSection(TaskSet):
    wait_time = constant(1)

    @task(10)
    def view_thread(self):
        pass

    @task
    def create_thread(self):
        pass

    @task
    def stop(self):
        self.interrupt()


class LoggedInUser(User):
    wait_time = constant(5)
    tasks = {ForumSection:2}

    @task
    def my_task(self):
        pass


'''2、 直接在User/TaskSet 类下内联 TaskSet，并使用task装饰器装饰'''


class MyUser(User):
    @task
    class MyTaskSet(TaskSet):
        pass


'''3、 TaskSet嵌套，模拟实际用户使用场景'''


'''4、 TaskSet使用interrupt()方法停止执行任务，并使用任务权重一起定义模拟用户离开任务的可能性'''


class RegisteredUser(User):
    @task
    class Forum(TaskSet):
        @task(5)
        def view_thread(self):
            pass

        @task(1)
        def stop(self):
            self.interrupt()

    @task
    def frontpage(self):
        pass


'''5、 引用用户实例(TaskSet.user)和父TaskSet实例(TaskSet.parent)'''


'''6、 SequentialTask​​Set类，顺序执行任务'''


def function_task(taskset):
    taskset.client.get("/3")


class SequenceOfTasks(SequentialTaskSet):
    @task
    def first_task(self):
        self.client.get("/1")
        self.client.get("/2")

    # you can still use the tasks property to specify a list of tasks
    tasks = [function_task]

    @task
    def last_task(self):
        self.client.get("/4")



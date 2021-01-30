from locust import HttpUser, constant, tag, task

'''3、 task任务装饰器的list、dict、weight测试，注意，函数要在用户类前面，否则引用不到'''


def test_task_def1():
    print('test_task_def1111')


def test_task_def2():
    print('test_task_def2222')


class test_task_list(HttpUser):
    # 测试task的列表、weight
    tasks = [test_task_def1]
    wait_time = constant(1)


class test_task_dict(HttpUser):
    # 测试task的字典、weight
    tasks = {test_task_def1: 1, test_task_def2: 3}
    wait_time = constant(1)


'''4、 tag标签装饰器测试'''


class test_tag(HttpUser):
    wait_time = constant(1)

    @tag('tag1')
    @task
    def task1(self):
        print('tag1')

    @tag('tag1', 'tag2')
    @task
    def task2(self):
        print('tag1 tag2')

    @tag('tag3')
    @task
    def task3(self):
        print('tag3')

    @task
    def task4(self):
        print('no tag')
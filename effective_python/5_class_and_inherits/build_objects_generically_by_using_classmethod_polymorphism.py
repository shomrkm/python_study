# -*- coding:utf-8 -*-

# - Python ではクラスに対して、__init__ という1つのコンストラクタしかサポートしていない
# - クラスに対して代わりのコンストラクタを定義するためには、@classmethod を使う
# - 具象サブクラスを作成して連携するジェネリックな方式を提供するには、クラスメソッドポリモルフィズムを使う

import os
import shutil
from threading import Thread

class InputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        with open(self.path) as f:
            return f.read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result



def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)



####################

import random

def write_test_files(tmp_dir):
    os.makedirs(tmp_dir)
    for i in range(100):
        with open(os.path.join(tmp_dir, str(i)), 'w') as f:
            f.write('\n' * random.randint(0, 100))


tmpdir = 'test_input'
config = {'data_dir': tmpdir}
write_test_files(tmpdir)
result = mapreduce(LineCountWorker, PathInputData, config)
print(f'There are {result} lines')
shutil.rmtree(tmpdir)

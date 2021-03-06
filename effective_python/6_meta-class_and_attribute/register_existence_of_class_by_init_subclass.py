# -*- coding:utf-8 -*-

# - クラス登録は、モジュール性の高い Python プログラムを構築するための、有用なパターンである
# - メタクラスで、規定クラスがサブクラスされるたびに登録コードを自動的に実行できる
# - クラス登録にメタクラスを使うと、必ず登録呼び出しを行うので、エラーをなくすことができる
# - 標準的なメタクラス機構よりも、__init_subclass__ を使うほうがより明確で、初心者にも理解しやすいので好ましい

import json

registry = {}
def register_class(target_class):
    registry[target_class.__name__] = target_class

class Serializable:
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args
            })

    def __repr__(self):
        name = self.__class__.__name__
        args_str = ','.join(str(x) for x in self.args)
        return f'{name}({args_str})'


class RegisteredSerializable(Serializable):
    def __init_subclass__(cls):
        super().__init_subclass__()
        register_class(cls)


def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class Point2D(RegisteredSerializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

class Vector1D(RegisteredSerializable):
    def __init__(self, magnitude):
        super().__init__(magnitude)
        self.magnitude = magnitude


print('# Point2D ###############')
before = Point2D(5,3)
print('Before:    ', before)
data = before.serialize()
print('Serialize: ', data)
after = deserialize(data)
print('After:     ', after)

print('# Vector1D ##############')
before = Vector1D(6)
print('Before:    ', before)
data = before.serialize()
print('Serialize: ', data)
after = deserialize(data)
print('After:     ', after)

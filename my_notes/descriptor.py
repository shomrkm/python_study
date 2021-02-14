# -*- coding:utf-8 -*-

class LoggedAgeAccess:

    def __set_name__(self, owner, name):
        print('__set_name__', name)
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        print(f'Accessing {self.public_name} giving {value}')
        return value

    def __set__(self, obj, value):
        print(f'Updating {self.public_name} to {value}')
        setattr(obj, self.private_name, value)


class Person:

    print('Person defined')
    name = LoggedAgeAccess()    # First descriptor instance
    age = LoggedAgeAccess()     # Second descriptor instance

    def __init__(self, name, age):
        self.name = name    # Calls the first descriptor
        self.age = age      # Calls the second descriptor

    def birthday(self):
        self.age += 1       # Calls both __get__() and __set__()


mary = Person('Mary M', 30)
mary.age
mary.birthday()



# Note:
# オブジェクトの属性にアクセスしたとき、以下のような順で処理が行われる
# 1. オブジェクトのクラスのデータ保持領域(クラスの__dict__)で要素が探索される
#    該当する要素が存在し、かつ __get__, __set__ 両方のメソッドを備えていれば、メソッドが呼ばれ戻り値が返される
# 2. オブジェクト固有のデータ保持領域(オブジェクトの__dict__)にある要素が探索される
# 3. オブジェクトのクラスのデータ保持領域(クラスの__dict__)で要素が探索される
#    該当する要素が見つかったら場合、
#    2-1. その要素オブジェクトが__get__メソッドを備えていれば、それが呼ばれる
#    2-2. その要素オブジェクトが__get__メソッドを備えていなければ、オブジェクトそのものが返される
# 4. 継承をたどってすべての親のデータ保持良識で要素が探索される
# 5. __getattr__() 関数があれば、呼び出しが発生する
# 6. AttributeError が送出される

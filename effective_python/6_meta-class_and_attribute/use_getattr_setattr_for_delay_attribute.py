# -*- coding:utf-8 -*-

# - オブジェクトの属性を遅延的にロードしたりほぞんしたりするには、__getattr_ と __setattr__ を使う
# - __getattr__は、見つからない属性にアクセスするときに一度だけ呼び出され、
#   __getattriubute__ は、属性がアクセスされるたびに呼び出されることを理解する
# - super() (すなわち object クラス) のメソッドを使ってインスタンス属性に直接アクセスことで、
#   __getattribute__ と __setattr__ とで無限再帰に入るのを避ける

class  LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = f'Value for {name}'
        setattr(self, name, value)
        return value

data = LazyRecord()
print('Before:', data.__dict__)
print('foo:   ', data.foo)
print('After: ', data.__dict__)

print('########################################')

class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f'* Called __getattr__({name!r})',
              f'populating instance dictionary')
        result = super().__getattr__(name)
        print(f'* Returning {result!r}')
        return result

# インスタンス辞書にないときだけ __getattr__ が呼ばれる
data = LoggingLazyRecord()
print('exists:      ', data.exists)
print('First foo:   ', data.foo)
print('Second foo:  ', data.foo)

print('########################################')

class ValidatingRecord:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print(f'* Called __getattribute__({name!r})')
        try:
            value = super().__getattribute__(name)
            print(f'* Found {name!r}, returning {value!r}')
            return value
        except AttributeError:
            value = f'Value for {name}'
            print(f'* Setting {name!r} to {value!r}')
            setattr(self, name, value)
            return value

data = ValidatingRecord()
print('exists:      ', data.exists)
print('First foo:   ', data.foo)
print('Second foo:  ', data.foo)
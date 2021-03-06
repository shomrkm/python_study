# -*- coding:utf-8 -*-

# - メタクラスは、クラスが完全に定義される前に、クラス属性の修正を可能にする
# - ディスクリプタとメタクラスとは、宣言的な振る舞いと実行時イントロスペクションのための強力なコンビである
# - ディスクリプタクラスで __set_name__ を定義すると、取り囲むクラスとその属性名についての処理ができる
# - ディスクリプタがクラスインスタンスの階層において、扱うデータを直接調べることで、
#   メモリリークと組み込みモジュール weakref の両方を避けることができる

class Field:
    def __init__(self):
        self.name = None
        self.internal_name = None

    def __set_name__(self, owner, name):
        # Fieldディスクリプタインスタンスを保持するクラス作成が作成されたとき、(ここでは Customer クラス作成時)
        # 保持されているすべてのディスクリプタインスタンスについて呼び出される
        self.name = name
        self.internal_name = '_' + name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Customer:
    # クラス属性
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()


cust = Customer()
print(f'Before: {cust.first_name!r} {cust.__dict__}')
cust.first_name = 'Euclid'
print(f'After:  {cust.first_name!r} {cust.__dict__}')

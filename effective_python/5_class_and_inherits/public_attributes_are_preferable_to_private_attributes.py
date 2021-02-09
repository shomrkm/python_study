# -*- coding:utf-8 -*-

# - プライベート属性は、Python コンパイラが厳密に強化して強制しているもの尾ではない
# - サブクラスを締め出すのではなく、内部APIと属性を利用できるように最初から考慮しておくこと
# - プライベート属性でアクセス制御するのは避け、保護フィールドについてドキュメンテーションで説明してサブクラスを使う

class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field


foo = MyObject()
foo.get_private_field()
# foo.__private_field # Error

print(foo.__dict__) # {'public_field': 5, '_MyObject__private_field': 10}
print(foo._MyObject__private_field) # 結局アクセスできる

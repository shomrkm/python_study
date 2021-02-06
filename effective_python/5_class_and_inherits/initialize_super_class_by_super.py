# -*- coding:utf-8 -*-

# Python の標準メソッドの解決順序（MRO）は、
# スーパークラスの初期化順序とダイヤモンドの継承の問題を解消する

# Old and Bad Style

class MyBaseClass:
    def __init__(self, value):
        self.value = value

class TimesSeven(MyBaseClass):
    def __init__(self, value):
       MyBaseClass.__init__(self, value)
       self.value *= 7

class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 9

class BadWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)

foo = BadWay(5)
print('Should be (5 * 7) + 9 = 44 but is', foo.value)


# Better Style

class TimesSevenCollect(MyBaseClass):
    def __init__(self, value):
       super().__init__(value)
       self.value *= 7

class PlusNineCollect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9

class GoodWay(TimesSevenCollect, PlusNineCollect):
    def __init__(self, value):
        super().__init__(value)

foo = GoodWay(5)
print('Should be 7 * (5 + 9) = 98 and is', foo.value)

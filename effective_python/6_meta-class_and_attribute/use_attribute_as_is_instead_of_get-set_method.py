# -*- coding:utf-8 -*-

# - 単純なパブリックな属性を使って新たなクラスのインターフェースを定義し、set や get メソッドは定義しない
# - 必要ならオブジェクトの属性にアクセスされたときの特別な振る舞いを @property を使って定義する
# - 驚き最小の原則に従い、@property メソッドで奇妙な副作用が生じるのを防ぐ
# - @property メソッドが高速なことを確かめる。遅かったり、複雑になったりする作業は通常のメソッドを使う


class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r = VoltageResistance(1e3)
print(f'Before: {r.current:.2f} amps')
r.voltage = 10
print(f'After:  {r.current:.2f} amps')

print('############################')

class BoundResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'ohms must be > 0; got {ohms}')
        self._ohms = ohms


r2 = BoundResistance(1e3)
# r2.ohms = 0  # Error


class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attrubute")
        self._ohms = ohms


r3 = FixedResistance(1e3)
# r3.ohms = 2e3   # Error


class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        # 悪い実装例
        self.voltage = self._ohms + self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

r4 = MysteriousResistor(10)
print(r4.__dict__)
r4.current = 0.01
print(f'Before: {r4.voltage:.2f}')
r4.ohms
print(f'After:  {r4.voltage:.2f}')


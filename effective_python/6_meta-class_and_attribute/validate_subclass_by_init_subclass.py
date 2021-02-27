# -*- coding:utf-8 -*-

# - メタクラスの __new__ メソッドは、class 文の本体全部が処理された後に実行される
# - クラスの定義後かつ作成される前に妥当性検証がや修正をするためにめたくらすを使うことができる
#   しかし、必要以上に複雑になることが多い
# - __init_subclass__ を使ってサブクラスを定義して、その方のオブジェクトが作られる前に、
#   正しく定義されることを確証できる
# - クラスの __init_subclasss__ 定義の中において、super().__init_subclass__ を呼び出して、
#   クラス階層の複数の階層と多重検証ができることを確かなものにする

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(f'* Running {meta}.__new__ for {name}')
        print('Bases:',bases)
        print(class_dict)
        return type.__new__(meta, name, bases, class_dict)


class MyClass(metaclass=Meta):
    stuff = 123

    def foo(self):
        pass

class MySubclass(MyClass):
    other = 567

    def bar(self):
        pass

c = MySubclass()

print('#############################')


class Polygon:
    sides = None    # サブクラスで指定しなければならない

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError('Polygon needs 3* sides')

    @classmethod
    def interior_angle(cls):
        return (cls.sides - 2) * 180

class Triangle(Polygon):
    sides = 3

class Rectangle(Polygon):
    sides = 4

class Nonagon(Polygon):
    sides = 9

assert Triangle.interior_angle() == 180
assert Rectangle.interior_angle() == 360
assert Nonagon.interior_angle() == 1260

## Error
#class Point(ValidatePolygon):
#    sides = 1

#########################


class Filled:
    color = None    # サブクラスで指定しなければならない
    
    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.color not in ('red', 'green', 'blue'):
            raise ValueError('Fills need a valid color')


class RedTriangle(Filled, Polygon):
    color = 'red'
    sides = 3

ruddy = RedTriangle()
assert isinstance(ruddy, Filled)
assert isinstance(ruddy, Polygon)

## Error
#class BlueLine(Filled, Polygon):
#    color = 'blue'
#    sides = 2

class BeigeSquare(Filled, Polygon):
    color = 'beige'
    sides = 4

# -*- coding:utf-8 -*-

# - ディスクリプタクラスを定義して、@property メソッドの振る舞いや確認作業を再利用する
# - WeakKeyDictionary を用いて、ディスクリプタクラスがメモリリークを起こさないようにする
# - __getattrubute__ が属性のゲッターやセッターのために
#   ディスクリプタプロトコルをどのように使っているかを理解して、予期せぬエラーを避ける

from weakref import WeakKeyDictionary

class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value

class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print('Writing', first_exam.writing_grade)
print('Science', first_exam.science_grade)

second_exam = Exam()
second_exam.writing_grade = 75
print(f'First {first_exam.writing_grade} is right')
print(f'Second {second_exam.writing_grade} is right')

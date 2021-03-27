# -*- coding:utf-8 -*-

# Description
# - Python の組み込み型で print を呼び出すと、人間が読める値の文字列が生成されるが、型情報は表示されない
# - Python の組み込み型で repr を呼び出すと、出力可能な値の文字列が生成される.
#   この repr 文字列を組み込み可能な関数 eval に渡すと、多くの場合、もとの値を取り戻すことができる
# - フォーマット文字列の %s は str 関数のように、人間が読める文字列を生成する.
#   フォーマット文字列の %r は repr 関数のように、出力可能文字列を生成する.
#   f 文字列は、!r 接頭辞を指定しない限り、人間が読める文字列生成する
# - クラスの出力可能表現をカスタマイズするために、__repr__ メソッドを定義して、より詳細なデバッグ情報を与えることができる


print(repr(5))
print(repr('5'))

print('%r' % 5)
print('%s' % '5')
print('%r' % '5')

int_value = 5
str_value = '5'
print(f'{int_value} == {str_value}')
print(f'{int_value!r} == {str_value!r}')


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'MyClass({self.x}, {self.y})'

obj = MyClass(1, 'bar')
print(obj)

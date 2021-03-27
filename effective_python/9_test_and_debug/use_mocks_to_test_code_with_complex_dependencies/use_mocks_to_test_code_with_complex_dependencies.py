# -*- coding:utf-8 -*-

import random
random.seed(1234)

import logging
from pprint import pprint
from sys import stdout as STDOUT

# 0. 一時ディレクトリに環境を準備する

import atexit
import gc
import io
import os
import tempfile

# プログラム終了時に一時フォルダを破棄する
TEST_DIR = tempfile.TemporaryDirectory()
atexit.register(TEST_DIR.cleanup)

# プログラム終了時にカレントディレクトリに戻る
OLD_CWD = os.getcwd()
atexit.register(lambda: os.chdir(OLD_CWD))
os.chdir(TEST_DIR.name)

# プログラム終了時にファイルを閉じる
def close_open_files():
    everything = gc.get_objects()
    for obj in everything:
        if isinstance(obj, io.IOBase):
            obj.close()

atexit.register(close_open_files)

###########################################
# 1. 以下は、データベースが実行されていないので失敗する
print('1 ###########################')

class DatabaseConnection:
    def __init__(self, host, port):
        pass

class DatabaseConnectionError(Exception):
    pass

def get_animals(database, species):
    # Query the Database
    raise DatabaseConnectionError('Not connected')
    # Return a list of (name, last_mealtime) tuples

try:
    database = DatabaseConnection('localhost', 4444)

    get_animals(database, 'Meerkat')
except:
    logging.exception('Expected')
else:
    assert False


###########################################
# 2. 実際にデータベースにコネクションを張らずに、Mock インスタンスを定義する
print('2 ###########################')

from datetime import datetime
from unittest.mock import Mock

mock = Mock(spec=get_animals)
expected = [
    ('Spot', datetime(2019, 6, 5, 11, 15)),
    ('Fluffy', datetime(2019, 6, 5, 12, 30)),
    ('Jojo', datetime(2019, 6, 5, 12, 45)),
]
mock.return_value = expected

try:
    # 間違った使い方(属性にアクセスしようとした場合など) をしたらエラーとなる
    mock.does_not_exist
except:
    logging.exception('expected')
else:
    assert False

# 正しい値が返ってくる
database = object()
result = mock(database, 'Meerkat')
assert result == expected

# モックに正しい引数が指定したかどうかは、assert_called_once_with メソッドを使う
try:
    mock.assert_called_once_with(database, 'Giraffe')
except:
    logging.exception('Expected')
else:
    assert False

# どんな引数でもOKな場合は、ANY を使う
from unittest.mock import ANY

mock = Mock(spec=get_animals)
mock('database 1', 'Rabbit')
mock('database 2', 'Bison')
mock('database 3', 'Meerkat')

mock.assert_called_with(ANY, 'Meerkat')

# 例外でモックを送出することもできる
try:
    class MyError(Exception):
        pass

    mock = Mock(spec=get_animals)
    mock.side_effect = MyError('Whoops! Big problem')
    result = mock(database, 'Meerkat')
except:
    logging.exception('Expected')
else:
    assert False


###########################################
# 3. 実際のユニットテストの使い方
print('3 ###########################')

# 3-1. すべてをキーワード専用引数で与えるやり方
# 出力が多くてテストする関数すべてに変更を加える必要がある

def get_food_period(database, species):
    # Query the Database
    pass
    # Return a time delta

def feed_animal(database, name, when):
    # Write to the Database
    pass

def do_rounds(database, species):
    now = datetime.datetime.utcnow()
    feeding_timedelta = get_food_period(database, species)
    animals = get_animals(database, species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_animal(database, name, now)
            fed += 1
    
    return fed

def do_rounds(database, species, *,
              now_func=datetime.utcnow,
              food_func=get_food_period,
              animals_func=get_animals,
              feed_func=feed_animal):
    now = now_func()
    feeding_timedelta = food_func(database, species)
    animals = animals_func(database, species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_func(database, name, now)
            fed += 1

    return fed

# Mock を準備
from datetime import timedelta

now_func = Mock(spec=datetime.utcnow)
now_func.return_value = datetime(2019, 6, 5, 15, 45)

food_func = Mock(spec=get_food_period)
food_func.return_value = timedelta(hours=3)

animals_func = Mock(spec=get_animals)
animals_func.return_value = [
    ('Spot', datetime(2019, 6, 5, 11, 15)),
    ('Fluffy', datetime(2019, 6, 5, 12, 30)),
    ('Jojo', datetime(2019, 6, 5, 12, 45)),
]

feed_func = Mock(spec=feed_animal)

# モックを do_rounds 関数に渡す
result = do_rounds(
    database,
    'Meerkat',
    now_func=now_func,
    food_func=food_func,
    animals_func=animals_func,
    feed_func=feed_func)

assert result == 2

# 依存関数へのすべての呼び出しが期待通りだったかを検証する
from unittest.mock import call

food_func.assert_called_once_with(database, 'Meerkat')
animals_func.assert_called_once_with(database, 'Meerkat')
feed_func.assert_has_calls(
    [
        call(database, 'Spot', now_func.return_value),
        call(database, 'Fluffy', now_func.return_value),
    ],
    any_order=True)



# 3-2. unittest.mock.patch を使うやり方
from unittest.mock import patch
print('Outside patch:', get_animals)
with patch('__main__.get_animals'):
    print('Inside patch: ', get_animals)
print('Outside again:', get_animals)


# datetime クラスは C 拡張モジュールで定義されているため、変更できない
# その場合は、以下の2通りの対応方法がある
# 3-2-1. ヘルパー関数を挟んで patch を使う
# 3-2-2. datetime.utcnow モックにだけキーワード専用引数を使う

try:
    fake_now = datetime(2019, 6, 5, 15, 45)
    with patch('datetime.datetime.utcnow'):
        datetime.utcnow.return_value = fake_now
except:
    logging.exception('Expected')
else:
    assert False

# 3-2-1. ヘルパー関数を挟んで patch を使う
def get_do_rounds_time():
    return datetime.datetime.utcnow()

def do_rounds(database, species):
    now = get_do_rounds_time()

with patch('__main__.get_do_rounds_time'):
    pass

# 3-2-2. datetime.utcnow モックにだけキーワード専用引数を使う
def do_rounds(database, species, *, utcnow=datetime.utcnow):
    now = utcnow()
    feeding_timedelta = get_food_period(database, species)
    animals = get_animals(database, species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_animal(database, name, now)
            fed += 1

    return fed



# 実際のモックを使ったテストコードの例

from unittest.mock import DEFAULT

with patch.multiple('__main__',
                    autospec=True,
                    get_food_period=DEFAULT,
                    get_animals=DEFAULT,
                    feed_animal=DEFAULT):
    # モック準備
    now_func = Mock(spec=datetime.utcnow)
    now_func.return_value = datetime(2019, 6, 5, 15, 45)
    get_food_period.return_value = timedelta(hours=3)
    get_animals.return_value = [
        ('Spot', datetime(2019, 6, 5, 11, 15)),
        ('Fluffy', datetime(2019, 6, 5, 12, 30)),
        ('Jojo', datetime(2019, 6, 5, 12, 45))
    ]

    # 関数の実行結果をテスト
    result = do_rounds(database, 'Meerkat', utcnow=now_func)
    assert result == 2
    # 依存関数の呼び出しをテスト
    get_food_period.assert_called_once_with(database, 'Meerkat')
    get_animals.assert_called_once_with(database, 'Meerkat')
    feed_animal.assert_has_calls(
        [
            call(database, 'Spot', now_func.return_value),
            call(database, 'Fluffy', now_func.return_value),
        ],
        any_order=True)
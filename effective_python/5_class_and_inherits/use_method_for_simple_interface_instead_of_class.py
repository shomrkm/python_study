# -*- coding:utf-8 -*-

# - Python コンポーネントの間の単純なインターフェースは、クラスを定義してインスタンス貸しなくても、たいてい関数で済ませられる。
# - Python では関数とメソッドの参照はファーストクラスなので、他の型同様、式中で使うことができる
# - 特殊メソッド __call__ を使用すると、クラスのインスタンスを Python の普通の関数として呼び出すことが可能になる
# - 状態を保守するために関数が必要な場合、状態を持つクロージャを定義する代わりに、__call__ メソッドを提供するクラスを定義することを考える

from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

# 関数を使って defaultdict の振る舞いをカスタマイズする
# missing メソッドというフックがクロージャで状態を持つ
# やや読みにくい

def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count    # ステートフルクロージャ
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    
    return result, added_count

# red, orange が追加されるときに missing() でカウントされる
result, count = increment_with_report(current, increments)
assert count == 2


# ヘルパークラス(CountMissing) を使って defaultdict の振る舞いをカスタマイズ
# 関数の例に比べ、コードとして読みやすい

class CountMissing:
    def __init__(self):
        self.added = 0 

    def __call__(self):
        self.added += 1
        return 0

# red, orange が追加されるときに CountMissing.__call__() でカウントされる
counter = CountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2

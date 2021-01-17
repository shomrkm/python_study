# -*- coding:utf-8 -*-

counter = {
    'pumpeernickel': 2,
    'sourdough': 1,
}
org = counter.copy()


key = 'wheat'

# キーがあるかどうかを調べる方法
if key in counter:
    count = counter[key]
else:
    count = 0
counter[key] = count + 1
print(counter)
counter = org.copy()

# キーが存在場合は Key Error 例外を送出する方法
try:
    count = counter[key]
except KeyError:
    count = 0
counter[key] = count + 1
print(counter)
counter = org.copy()

# get を使用する方法 (これが最も短く正確なコード)
# get の第2引数は Key が存在しなかった場合に返すデフォルト値)
count = counter.get(key, 0)
counter[key] = count + 1
print(counter)

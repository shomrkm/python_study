# -*- coding:utf-8 -*-

import tracemalloc

tracemalloc.start(10)               # スタックの深さ設定
time1 = tracemalloc.take_snapshot() # スナップショット前

import waste_memory

x = waste_memory.run()              # デバッグ利用
time2 = tracemalloc.take_snapshot() # スナップショット後

stats = time2.compare_to(time1, 'lineno')   # スナップショット比較
for stat in stats[:3]:
    print(stat)

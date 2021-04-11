# -*- coding:utf-8 -*-

import waste_memory
import tracemalloc

tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()


x = waste_memory.run()
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, 'traceback')
top = stats[0]
print('Biggest offender is:')
print('\n'.join(top.traceback.format()))

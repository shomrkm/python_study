# -*- coding:utf-8 -*-

# e.g. ソフトウェアラジオを使って信号を送出するプログラム


import math
def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output

def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')

def run(it):
    for output in it:
        transmit(output)

print(f'Run run().')
run(wave(3.0, 8))

print(f'------------------------------------------')

####
# 以下、send メソッドを理解するためのテスト

def my_generator():
    for i in range(10):
        num = yield i
        print(f'my_generator(): {num}')

print(f'Run my test code.')
it = iter(my_generator())
print(it.send(None))
print(it.send(100))
print(next(it))
print(next(it))
print(it.send(200))
print(it.send(None))


print(f'------------------------------------------')

####
# 最初のプログラムを外から波形の振幅を変動できるように変更

def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield # 最初の振幅を受け取る
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output # 次の振幅を受け取る

def run_modulating(it):
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)

print(f'Run run_modulating().')
run_modulating(wave_modulating(12))


def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)

# complex_wave_modulating() の yield from が終了するたびに次に移る(=もとの値のない yield 文から始まる)
# のでそのたびに None が出力される
run_modulating(complex_wave_modulating())

print(f'------------------------------------------')


# このような場合は、send()は避けて実装するのがベストプラクティス

def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it) # 次の入力取得
        output = amplitude * fraction
        yield output

def complex_wave_modulating(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)

def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    it = complex_wave_modulating(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)

run_cascading()
print(f'Run run_cascading().')

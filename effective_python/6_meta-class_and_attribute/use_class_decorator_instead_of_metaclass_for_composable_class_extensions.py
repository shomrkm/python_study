# -*- coding:utf-8 -*-

# - クラスデコレータは class インスタンスを引数として、新たなクラスまたは元のクラスの修正バージョンを返す簡単な関数だ
# - クラスデコレータは、最小の定型文ですべてのメソッドまたは属性を修正したい場合に役に立つ
# - メタクラスは、簡単に合成できないが、多くのクラスデコレータがクラスの拡張に問題なく使うことができる

from functools import wraps

def trace_func(func):
    if hasattr(func, 'tracing'):    # 一度だけデコレート 
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            result = e
            raise
        finally:
            print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')

    wrapper.tracing = True
    return wrapper


class TraceDict(dict):
    @trace_func
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    @trace_func
    def __setitem__(self, *args, **kargs):
        return super().__setitem__(*args, **kargs)

    @trace_func
    def __getitem__(self, *args, **kargs):
        return super().__getitem__(*args, **kargs)

trace_dict = TraceDict([('hi', 1)])
trace_dict['there'] = 2
trace_dict['hi']
try:
    trace_dict['does not exist']
except KeyError:
    pass    # 期待通り


print('###############################')


import types

trace_types = (
    types.MethodType,
    types.FunctionType,
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
    types.MethodDescriptorType,
    types.ClassMethodDescriptorType
)

class TraceMeta(type):
    def __new__(meta, name, bases, class_dict):
        klass = super().__new__(meta, name, bases, class_dict)

        for key in dir(klass):
            value = getattr(klass, key)
            if isinstance(value, trace_types):
                wrapped = trace_func(value)
                setattr(klass, key, wrapped)

        return klass

class TraceDict2(dict, metaclass=TraceMeta):
    pass

trace_dict = TraceDict2([('hi', 1)])
trace_dict['there'] = 2
trace_dict['hi']
try:
    trace_dict['does not exist']
except KeyError:
    pass    # 期待通り

print('###############################')


def trace(klass):
    for key in dir(klass):
        value = getattr(klass, key)
        if isinstance(value, trace_types):
            wrapped = trace_func(value)
            setattr(klass, key, wrapped)
    return klass


@trace
class TraceDict3(dict):
    pass

trace_dict = TraceDict3([('hi', 1)])
trace_dict['there'] = 2
trace_dict['hi']
try:
    trace_dict['does not exist']
except KeyError:
    pass    # 期待通り

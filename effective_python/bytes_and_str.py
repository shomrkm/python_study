# -*- coding:utf-8 -*-

def to_str(bytes_or_str):
    ''' str のインスタンスを返す '''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_str(b'foo')))
print(repr(to_str('bar')))


def to_bytes(bytes_or_str):
    ''' bytes のインスタンスを返す '''
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))



# Note:
#  repr(objects): デバッグ用に eval　関数で評価可能な文字列を返す
# -*- coding:utf-8 -*-

def safe_division(numerator, denominator, /,
                  ndigits=10, *,
                  ignore_overflow=False,
                  ignore_zero_division=False):
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division(22,7)
print(result)
result = safe_division(22, 7, 5)
print(result)

result = safe_division(22, 7, ndigits=3)
print(result)

result = safe_division(1.0, 10**500, ignore_overflow=True)
print(result)
# result = safe_division(1.0, 10**500)  # 例外

result = safe_division(1.0, 0, ignore_zero_division=True)
print(result)
# result = safe_division(1.0, 0)  # 例外

# ignore_overflow, ignore_zero_division はキーワード引数以外で指定不可
# result = safe_division(22, 7, 10, False, False)

# 第1,2引数はキーワード引数では指定不可
# result = safe_division(numerator=22, denominator=7)

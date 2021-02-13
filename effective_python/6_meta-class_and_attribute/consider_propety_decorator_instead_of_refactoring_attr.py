# -*- coding:utf-8 -*-

# - @property を使って既存のインスタンス属性に新たな機能を追加する
# - @property を使って、より良いデータモデルへと逐次改善する
# - @property をあまり使いすぎると感じるようになったら、
#   そのクラスとすべての呼び出し元をリファクタリングすることを考える

from datetime import datetime, timedelta

class Bucket:
    ''' Water leak bucket '''
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return f'Bucket(quota={self.quota})'


def fill(bucket, amount):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount

def dedect(bucket, amount):
    ''' Return whether you can get the required amount of water from bucket or not.'''
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        return False    # There is no water in the period.
    if bucket.quota - amount < 0:
        return False    # Not enough water.
    bucket.quota -= amount
    return True          # Bucket is full and get the water from bucket.


bucket = Bucket(60)
fill(bucket, 100)
print(bucket)

if dedect(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print(bucket)

if dedect(bucket, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print(bucket)


print('#############################')


class NewBucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0
    
    def __repr__(self):
        return (f'NewBucket(max_quota={self.max_quota}, quota_consumed={self.quota_consumed})')

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed
        
    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            # Reset quota
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # Set the new quota for new period
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            # Consume the quota in the period
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


bucket = NewBucket(60)
fill(bucket, 100)
fill(bucket, 10)
print(bucket)

if dedect(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print(bucket)

if dedect(bucket, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print(bucket)
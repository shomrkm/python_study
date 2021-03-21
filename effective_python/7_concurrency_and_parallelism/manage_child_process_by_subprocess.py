# -*- coding:utf-8 -*-

# Requirment
# - OpenSSL
#   インストール後、下記のコマンドでパスを通して置く必要あり。
#   $env:path = $env:path + ";C:\Program Files\OpenSSL-Win64\bin"

# Reference
# - Effective Python 内のコードは、Windows 環境だと動かない部分もあるので、以下も参照する
#   https://github.com/bslatkin/effectivepython/blob/master/example_code/item_52.py


import subprocess
import os
import time


print('# Example of subprocess.run().')

# 環境変数を変更して、PowerShell を使うように設定
# COMSPEC: C:\WINDOWS\system32\cmd.exe -> powershell
os.environ['COMSPEC'] = 'powershell'

# run メソッドはコマンドが終了してはじめて制御がPython スクリプトに戻ってくる
result = subprocess.run(
    ['echo', 'Hello from the child!'],
    capture_output=True,    # 標準出力, 標準エラー出力ともにPIPEが指定される
    shell=True,
    encoding='utf-8'
)

result.check_returncode()   # 例外がないときは、クリーン終了
print(result.stdout)

print('###################')
print('# Example of subprocess.Popen().')

# Popen クラスを使って子プロセスを作ると、Python が他の仕事をしている間、
# 子プロセスの状態を定期的にポーリングしてチェックできる
proc = subprocess.Popen(['Sleep', '1'], shell=True)
while proc.poll() is None:
    print('Working...')
    time.sleep(0.3)
print('Exit status', proc.poll())

print('-------------------')
print('# Waiting child process by communicate().')

# 子プロセスを親プロセスから切り離すと、親プロセスが自由になって、
# 多数の子プロセスを並列に実行できる
start = time.time()
sleep_procs = []
for _ in range(10):
    proc = subprocess.Popen(['sleep', '1'], shell=True)
    sleep_procs.append(proc)

# communite メソッドで、子プロセスがI/Oを終えて終了するのを待つ
for proc in sleep_procs:
    proc.communicate()

end = time.time()
delta = end - start
print(f'Finished in {delta:.3} seconds')

print('###################')
# 子プロセスを使ってデータ暗号化を行う例
# OpenSSL を使用するため、下記のコマンドでパスを通して置く必要あり。
#   $env:path = $env:path + ";C:\Program Files\OpenSSL-Win64\bin"
print('# Example of encrypt data.')


def run_encrypt(data):
    env = os.environ.copy()
    env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
    # OpenSSL を使ったデータ暗号化の子プロセス作成 (3DES というやり方で暗号化)
    # openssl enc -des3 -pass env:password
    # -> "enc -des3" : DES3 という暗号化のやり方を使うという意味
    # -> "-pass env:password": 環境変数 password をパスワードとして使用するという意味
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,      # 標準入力へのパイプ指定
        stdout=subprocess.PIPE      # 標準出力にパイプ指定 (Pythonコード内で取得する)
        )
    proc.stdin.write(data)
    proc.stdin.flush()  # 子の入力を確実にする
    return proc

procs = []
for _ in range(3):
    data = os.urandom(10)       # 暗号に関数用途に適した10バイトのランダムな文字列を返す
    proc = run_encrypt(data)
    procs.append(proc)

for proc in procs:
    out, _ = proc.communicate()
    print(out[-10:])


print('###################')
# 子プロセスの出力を他の子プロセスの入力につなげていって、
# 並列プロセスの連鎖を作ることもできる
print('# Example of encrypt data -> hash encrypted data')

def run_hash(input_stdin):
    return subprocess.Popen(
        ['openssl', 'dgst', '-whirlpool', '-binary'],
        stdin=input_stdin,
        stdout=subprocess.PIPE
    )

encrypt_procs =[]
hash_procs = []
for _ in range(3):
    data = os.urandom(100)

    encrypt_proc = run_encrypt(data)
    encrypt_procs.append(encrypt_proc)

    hash_proc = run_hash(encrypt_proc.stdout)
    hash_procs.append(hash_proc)

    # 子プロセスが入力ストリームを取り込み
    # communicate() メソッドがうっかりして子から入力を横取りしないようにする
    # また SIGPIPE がダウンストリームプロセスが死ぬと
    # アップストリームプロセス伝播する
    encrypt_proc.stdout.close()
    encrypt_proc.stdout = None


# データ暗号化
for proc in encrypt_procs:
    proc.communicate()
    assert proc.returncode == 0

# 暗号化された出力からハッシュコード生成
for proc in hash_procs:
    out, _ = proc.communicate()
    print(out[-10:])


print('###################')
print('# Example of using communicate with timeout')

proc = subprocess.Popen(['sleep', '10'], shell=True)
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()
print('Exit status', proc.poll())

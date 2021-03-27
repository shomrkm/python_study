# -*- coding:utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, main

class EnviromentTest(TestCase):
    ''' 各テストの前に一時的なディレクトリを作成して、テスト終了後に破棄する
    '''
    def setUp(self):
        self.test_dir = TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)

    def setDown(self):
        self.test_dir.cleanup()

    def test_modify_file(self):
        with open(self.test_path / 'data.bin' , 'w') as f:
            f.write('hello')


if __name__ == '__main__':
    main()

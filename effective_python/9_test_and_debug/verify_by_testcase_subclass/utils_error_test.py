# -*- coding:utf-8 -*-

from unittest import TestCase, main
from utils import to_str

class UtilsErrorTestCase(TestCase):
    def test_to_str_bad(self):
        with self.assertRaises(TypeError):
            to_str(object())

    def test_to_str_bad_encoding(self):
        # with ステートメントを使って、どこで例外が発生すると期待するのかを明確にする
        with self.assertRaises(UnicodeDecodeError):
            to_str(b'\xfa\xfa')


if __name__ == '__main__':
    main()
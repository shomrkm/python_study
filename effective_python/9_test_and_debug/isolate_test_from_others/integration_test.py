# -*- coding:utf-8 -*-

from unittest import TestCase, main

# setUpModule, tearDownModule は unittest で一度だけ実行される
# setUp, setDown は各テストメソッドの前後に実行される

def setUpModule():
    print('* Module setup')

def tearDownModule():
    print('* Module clean-up')

class IntegrationTest(TestCase):
    def setUp(self):
        print('* Test setup')

    def tearDown(self):
        print('* Test clean-up')

    def test_end_to_end1(self):
        print('* Test 1')

    def test_end_to_end2(self):
        print('* Test 2')

if __name__ == '__main__':
    main()

# -*- coding:utf-8 -*-

import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Shotaro', 'Murakami', 50000)
        self.emp_2 = Employee('Hitomi', 'Fujimura', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Shotaro.Murakami@email.com')
        self.assertEqual(self.emp_2.email, 'Hitomi.Fujimura@email.com')

        self.emp_1.first = 'Jin'
        self.emp_2.first= 'Rieko'

        self.assertEqual(self.emp_1.email, 'Jin.Murakami@email.com')
        self.assertEqual(self.emp_2.email, 'Rieko.Fujimura@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Shotaro Murakami')
        self.assertEqual(self.emp_2.fullname, 'Hitomi Fujimura')

        self.emp_1.first = 'Jin'
        self.emp_2.first= 'Rieko'

        self.assertEqual(self.emp_1.fullname, 'Jin Murakami')
        self.assertEqual(self.emp_2.fullname, 'Rieko Fujimura')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
    
    def test_monthly_schedule(self):
        # employee.requests.get() メソッドをモックへ置き換え
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            # requests.get() が想定通りの引数で呼ばれているかテスト
            mocked_get.assert_called_with('http://company.com/Murakami/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Fujimura/June')
            self.assertEqual(schedule, 'Bad Response!')



if __name__ == '__main__':
    unittest.main()

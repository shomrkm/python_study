# -*- coding:utf-8 -*-
import sys
import datetime

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt

    # Additional constructors
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        return day.weekday() != 5 and day.weekday() != 6


def main():
    emp_str_1 = 'Shotaro-Murakami-60000'
    emp_1 = Employee.from_string(emp_str_1)

    my_date = datetime.date(2020, 8, 23)
    print(Employee.is_workday(my_date))


if __name__ == '__main__':
	sys.exit(main())
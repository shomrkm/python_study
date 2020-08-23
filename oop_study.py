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


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last ,pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    raise_amt = 1.10

    def __init__(self, first, last ,pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



def main():
    dev_1 = Developer('Shotaro', 'Murakami', 50000, 'Python')
    dev_2 = Developer('Test', 'Employee', 55000, 'C++')

    mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
    mgr_1.print_emps()
    print('---')
    mgr_1.add_emp(dev_2)
    mgr_1.print_emps()
    print('---')
    mgr_1.remove_emp(dev_1)
    mgr_1.print_emps()



if __name__ == '__main__':
	sys.exit(main())
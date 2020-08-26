# -*- coding:utf-8 -*-
import sys
import datetime

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

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

    # Special(Magic/Dunder) Methods
    def __repr__(self):
        return "'{}' '{}' {}".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {} - {}'.format(self.fullname(), self.email, 'Employee')



class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last ,pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __repr__(self):
        return "'{}' '{}' {} {}".format(self.first, self.last, self.pay, self.prog_lang)

    def __str__(self):
        return '{} - {} - {}'.format(self.fullname(), self.email, 'Developer')


class Manager(Employee):
    raise_amt = 1.10

    def __init__(self, first, last ,pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def __repr__(self):
        emp_str = '\n'
        for emp in self.employees:
            emp_str += '-->' + emp.__repr__() + '\n'
        return "'{}' '{}' {} {}".format(self.first, self.last, self.pay, emp_str)

    def __str__(self):
        return '{} - {} - {}'.format(self.fullname(), self.email, 'Manager')

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
    mgr_1 = Manager('Test', 'Employee', 80000, [dev_1])
    print(mgr_1.__repr__())

    dev_1.fullname = 'Hitomi Murakami'
    print(dev_1.fullname)
    del dev_1.fullname

    person = Employee('Yasuyuki', 'Chinen', 10000)
    print(person.fullname)



if __name__ == '__main__':
	sys.exit(main())
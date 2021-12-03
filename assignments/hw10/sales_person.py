"""
Name: Caroline Greer
sales_person.py

Problem: write a program that encapsulates data for a sales person

Certification of Authenticity:
I certify that this assignment is my work
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales = sale

    def total_sales(self):
        total = 0
        for num in self.sales:
            total += num
        return float(total)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if sum(self.sales) > quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        elif other.total_sales() < self.total_sales():
            return 1
        else:
            return 0

    def __str__(self):
        return "{0}-{1}:{2}".format(self.employee_id, self.name, self.sales)

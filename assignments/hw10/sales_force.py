from hw10.sales_person import *

"""
Name: Caroline Greer
sales_force.py

Problem: write a program that encapsulates data for a sales person

Certification of Authenticity:
I certify that this assignment is my work
"""


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        text = open(file_name, "r")
        for line in text:
            employee_id, name, sales = line.split(",")
            person = SalesPerson(int(employee_id), name)
            ind_sale = sales.split()
            for i in ind_sale:
                person.enter_sale(int(i))
            self.sales_people.append(person)
        text.close()

    def quota_report(self, quota):
        report = []
        for i in self.sales_people:
            report.append([i.met_quota(quota), i.get_id, i.get_name(), i.get_sales()])

    def top_seller(self):
        maxi = self.sales_people[0].total_sales()
        for i in range(len(self.sales_people)):
            if self.sales_people[i].total_sales() >= maxi:
                maxi = self.sales_people[i].total_sales()
        top_sel = []
        for x in range(len(self.sales_people)):
            if maxi == self.sales_people[x].total_sales():
                top_sel.append(self.sales_people[x].total_sales())
        return top_sel

    def individual_sales(self, employee_id):
        for i in self.sales_people:
            if employee_id == self.sales_people[i].get_id():
                return self.sales_people[i]
        return

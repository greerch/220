"""
Name: Caroline Greer
lab8.py

Discription: Solve the problems for lab 8

Certification of authenticity:
I certify that this assignment is entirely my own work
"""
from encryption import encode
from encryption import encode_better

def number_words(in_file_name, out_file_name):
    var = open(in_file_name, "r")
    out_file = open(out_file_name, 'w')

    for line in var:
        seperate = line.split()
        num = 1
        for i in range(len(seperate)):
            value = seperate[i]
            print(str(num) + " " + value, file=out_file, end='\n')
            num = num + 1

    var.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    var = open(in_file_name, "r")
    out_file = open(out_file_name, 'w')

    employee_raise = 1.65
    for line in var:
        first_name, last_name, hourly_wage, number_of_hours_worked = line.split(' ')
        employee_raise = eval(hourly_wage) + employee_raise
        new_pay = employee_raise * int(number_of_hours_worked)
        rounded_pay = round(new_pay, 2)
        print(first_name + " " + last_name + ": " + str(rounded_pay), file=out_file, end='\n')

    var.close()
    out_file.close()


def calc_check_sum(isbn):
    mod = 10
    final = 0
    checksum = " "
    for i in range(len(isbn)):
        value = mod * int(isbn[i])
        final = final + value
        mod = mod - 1
        checksum = final
    return checksum


def send_message(file, friend):
    new_file = friend + ".txt"
    in_file = open(file, 'r')
    out_file = open(new_file, 'w')

    data = in_file.read()
    print(data, file=out_file, end='\n')

    in_file.close()
    out_file.close()


def send_safe_message(file, friend, key):
    new_file = friend + ".txt"
    in_file = open(file, 'r')
    out_file = open(new_file, 'w')

    data = in_file.read()
    encoded = encode(data, key)
    print(encoded, file=out_file, end='\n')

    in_file.close()
    out_file.close()


def send_uncrackable_message(file, friend, pad):
    new_file = friend + ".txt"
    in_file = open(file, 'r')
    out_file = open(new_file, 'w')
    pad_file = open(pad, 'r')

    data = in_file.read()
    key = pad_file.read()
    encoded = encode_better(data, key)
    print(encoded, file=out_file, end='\n')

    in_file.close()
    out_file.close()




def main():
    number_words("Walrus.txt", "Walrus_close.txt")
    hourly_wages("hourly_wages.txt", "updated_wages.txt")
    calc_check_sum("0072946520")
    send_message("message.txt", "Alex")
    send_safe_message("secret_message.txt", "MaryBeth", 3)
    send_uncrackable_message("safest_message.txt", "Gracie", "pad.txt")

    pass

main()
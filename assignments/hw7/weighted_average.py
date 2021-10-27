"""
Name: Caroline Greer
weighted_average.py

Problem: write a program to calculates the weighted average

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    class_sum = 0
    counter = 0
    for line in in_file:
        name, numbers = line.split(':')
        num = numbers.split()
        weight_sum = 0
        value = 0
        for i in range(0, len(num), 2):
            weight_sum += eval(num[i])
        if weight_sum < 100:
            print(name + "'s average: Error: The weights are less than 100.", file=out_file, end='\n')
        elif weight_sum > 100:
            print(name + "'s average: Error: The weights are more than 100.", file=out_file, end='\n')
        else:
            counter = 1 + counter
            for i in range(0, len(num), 2):
                value += eval(num[i + 1]) * eval(num[i])
            person_avg = value / 100
            class_sum = class_sum + person_avg
            print(name + "'s average: " + str(round(person_avg, 1)), file=out_file, end='\n')
    print("Class average: " + str(round(class_sum/counter, 1)), file=out_file, end='\n')

    in_file.close()
    out_file.close()

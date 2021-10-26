"""
Name: Caroline Greer
weighted_average.py

Problem: write a program to calculates the weighted average

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

def weighted_average(in_file_name, out_file_name):
    in_file_name = input('What file are the grades in?')
    out_file_name = input('What is the output file?')

    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    for line in in_file:
        lines = line.split()
        weight_sum = 0
        values_sum = 0
        for i in range(2, len(lines), 2):
            weight_sum = lines[i] + weight_sum
        for x in range(3, len(lines), 2):
            values_sum = lines[x] + values_sum



    if weight_sum == 100:
        print (weighted_average, file = out_file, end='/n')

    elif weight_sum >= 100:
        print("Error: The weights are more than 100", file = out_file, end='/n')

    else:
        print("Error: The weights are less than 100", file = out_file, end='/n')

    in_file.close()
    out_file.close()


main():
    weighted_average('grades.txt', 'avg.txt')

if __name__ == '__main__':
    main
"""
Name: Caroline Greer
mean.py

Problem: Compute different averages

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

def main():
    num_values = eval(input("Enter the values to be entered: "))
    tot = 0
    den = 0
    between = 1
    for _ in range(num_values):
        enter_value = eval(input("Enter value: "))
        sqrt_numbers = (enter_value ** 2)
        tot = tot + sqrt_numbers
        den = den + (1 / enter_value)
        between = between * enter_value
    inside = tot / num_values
    rsm_average = inside ** (1 / 2)
    print(round(rsm_average, 3))
    harm_mean = num_values / den
    print(round(harm_mean, 3))
    geo_mean = between ** (1 / num_values)
    print(round(geo_mean, 3))

if __name__ == "__main__":
    main()

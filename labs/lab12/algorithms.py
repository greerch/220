def read_data(filename):
    file = open(filename, "r")
    file = file.read()
    lines = file.split()
    num = 0
    while num < len(lines):
        lines[num] = eval(lines[num])
        num += 1
    return lines


def is_in_linear(search_val, values):
    num = 0
    while num < len(values):
        if search_val == values[num]:
            return True
        num += 1
    return False

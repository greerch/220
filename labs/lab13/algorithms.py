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


def is_in_binary(search_val, values):
    left = 0
    right = len(values) - 1
    while left <= right:
        middle = (right + left) // 2
        middle_value = values[middle]
        if search_val == middle_value:
            return True
        elif search_val < middle_value:
            right = middle - 1
        elif search_val > middle_value:
            left = middle + 1
    return False


def selection_sort(values):
    n = len(values)
    for bottom in range(n-1):
        lowest = bottom
        for i in range(bottom + 1, n):
            if values[i] < values[lowest]:
                lowest = i
        values[bottom], values[lowest] = values[lowest], values[bottom]


def rect_sort(rectangles):
    area_list = []
    for i in range(len(rectangles)):
        area_list.append(calc_area(rectangles[i]))
    selection_sort(area_list)


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    p1x, p1y = p1.getX(), p1.getY()
    p2x, p2y = p2.getX(), p2.getY()
    base = abs(p1x - p2x)
    height = abs(p1y - p2y)
    area = base * height
    return area

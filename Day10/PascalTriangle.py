rows = 10

triangle = [[0, 0],
            [0, 1, 0],
            [0, 1, 2, 1, 0],
            [0, 1, 3, 3, 1, 0]]


def make_pascal_triangle(previous_level=[ 1, 0]):
    global rows
    if rows == 0:
        return
    current_level = previous_level.copy()
    new_level = []
    new_level.append(0)
    for n in range(len(current_level) - 1):
        value1 = current_level[n] + current_level[(n + 1)]

        new_level.append(value1)
    new_level.append(0)
    rows -= 1
    print(current_level)
    return make_pascal_triangle(new_level)


make_pascal_triangle()

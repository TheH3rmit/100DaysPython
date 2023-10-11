def make_pascal_triangle(rows):
    if rows < 0:
        raise ValueError("number of rows is negative")
    if rows == 0:
        return []
    if rows == 1:
        return [[1]]

    current_level = make_pascal_triangle(rows - 1)
    new_level = [1]

    for n in range(len(current_level[-1]) - 1):
        new_level.append(current_level[-1][n] + current_level[-1][n + 1])

    new_level.append(1)
    triangle = current_level
    triangle.append(new_level)
    return triangle

for k in make_pascal_triangle(10):
    print(k)

def print_triangle(size, character):
    triangle = ''
    for i in range(size):
        triangle += " " * (size - i - 1)
        triangle += character  + character * (2 * i)
        if i != size - 1:
            triangle += "\n"
    return triangle
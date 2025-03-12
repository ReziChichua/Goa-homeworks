#1
def count_red_beads(n):
    if n < 2:
        return 0
    return 2 * (n - 1)

#2
def generate_shape(n):
    return '\n'.join(['+' * n] * n)

#3
def bumps(road):
     return "Car Dead" if road.count('n') > 15 else "Woohoo!"

#4
def adjacent_element_product(array):
    return max(array[i] * array[i + 1] for i in range(len(array) - 1))

#5
def filter_string(st):
    return int(''.join(filter(str.isdigit, st)))
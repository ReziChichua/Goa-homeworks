#1
def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
    diamond_str = ''
    for i in range(1, n + 1, 2):
        diamond_str += ' ' * ((n - i) // 2) + '*' * i + '\n'
    for i in range(n - 2, 0, -2):
        diamond_str += ' ' * ((n - i) // 2) + '*' * i + '\n'
    return diamond_str

#2
def matrix_addition(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

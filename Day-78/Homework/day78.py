#1
def likes(names):
    n = len(names)
    if n == 0:
        return "no one likes this"
    elif n == 1:
        return f"{names[0]} likes this"
    elif n == 2:
        return f"{names[0]} and {names[1]} like this"
    elif n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {n - 2} others like this"


#2
def dig_pow(n, p):
    total = sum(int(digit) ** (p + i) for i, digit in enumerate(str(n)))
    return total // n if total % n == 0 else -1


#3
def matrix_division(a, b):
    if len(a) != len(b) or any(len(row_a) != len(row_b) for row_a, row_b in zip(a, b)):
        return None
    result = []
    for row_a, row_b in zip(a, b):
        row = []
        for val_a, val_b in zip(row_a, row_b):
            if val_b == 0:
                return None
            row.append(val_a / val_b)
        result.append(row)
    return result


#4
def draw_stairs(n):
    return '\n'.join(' ' * i + 'I' for i in range(n))


#5
def usdcny(usd):
    cny = usd * 6.75
    return f"{cny:.2f} Chinese Yuan"

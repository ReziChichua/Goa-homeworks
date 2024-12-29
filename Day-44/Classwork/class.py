#1
def friend(x):
    return [i for i in x if len(i) == 4] 

#2
def maskify(cc):
    lenght = len(cc)
    if lenght > 4:
        last = cc[-4:]
        return "#" * (lenght - 4) + last
    else:
        return cc

#3
def add_binary(a,b):
    return bin(a + b)[2:]

#4
def validate_pin(pin):
    if len(pin) not in (4, 6):
        return False
    for c in pin:
        if c not in '0123456789':
            return False
    return True

#5
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
#2
def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    return False


#3
def count_sheep(n):
    result = ""
    for i in range(1, n + 1):
        result += f"{i} sheep..."
    return result


#4
def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'
    
#5
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'
    




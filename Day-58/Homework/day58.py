#1
def who_is_paying(name):
    return [name, name[:2]] if len(name) > 2 else [name]

#2
def odd_count(n):
    return n // 2

#3
def is_uppercase(inp):
    return inp == inp.upper()

#4
def grader(score):
    if score > 1 or score < 0.6:
        return "F"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    
#5
def if_chuck_says_so():
    return 1 == 0
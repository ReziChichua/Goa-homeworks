#1
def high_and_low(numbers):
    number_list = [int(num) for num in numbers.split()]
    
    highest = max(number_list)
    lowest = min(number_list)

    return f"{highest} {lowest}"

#2
def filter_list(l):
    return [i for i in l if type(i) == int]

#3
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))


#4
def is_square(n):    
    if n < 0:
        return False
    return n ** 0.5 %1 == 0.00


#5
def get_middle(s):
    length = len(s)
    if length % 2 != 0:
        return s[length // 2]
    else:
        return s[(length // 2) - 1:(length // 2) + 1]
    




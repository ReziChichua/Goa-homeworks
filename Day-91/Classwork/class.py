#1
def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))

#2
def mouth_size(animal): 
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"
    
#3
def nth_even(n):
    return 2 * (n-1)


#4
def replace_exclamation(st):
    res = []
    for i in st:
        if i in "aeiouAEIOU":
            res.append("!") 
        else:
            res.append(i) 
    return "".join(res)

#5
def unusual_five():
    return len("aaaaa")

# 7 kyu
#1
def row_sum_odd_numbers(n):
    return n ** 3

#2
def nb_year(p0, percent, aug, target):
    years = 0
    while p0 < target:
        p0 += int(p0 * percent / 100) + aug
        years += 1
    return years

#3
def number(bus_stops):
    return sum(i - x for i, x in bus_stops)

#4
def odd_or_even(arr):
    if arr == [0]:
        return "even"
    elif sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"
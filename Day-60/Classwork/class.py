#1
def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

#2
def likes(names):
    n = len(names)
    if n == 0:
        return "no one likes this"
    if n == 1:
        return f"{names[0]} likes this"
    if n == 2:
        return f"{names[0]} and {names[1]} like this"
    if n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {n-2} others like this"
    
#3
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
        

#4
def move_zeros(lst):
    non_zeros = [x for x in lst if x != 0] 
    zeros = [0] * (len(lst) - len(non_zeros)) 
    return non_zeros + zeros
#1
def find_multiples(integer, limit):
    multiples = []
    for i in range(integer, limit + 1, integer):
        multiples.append(i)
    return multiples

#2
a = "code"
b = "wa.rs"
name = a + b


#3
def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res.append(i)
        i += 1
    return res


#4
def xor(a,b):
    return a != b

#5
def get_real_floor(n):
    if n <= 0:
        return n
    elif n < 13:
        return n - 1
    else:
        return n - 2
    

#6
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [i for i in birds if i not in geese]

#7
def divisible_by(numbers, divisor):
    return [i for i in numbers if i % divisor == 0]

#8
def name_shuffler(str_):
    first, last = str_.split()  
    return f"{last} {first}"


#9
def pipe_fix(nums):
    return list(range(min(nums), max(nums) + 1))

#10
def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n < 10:
        return n * 95 
    else:
        return n * 90
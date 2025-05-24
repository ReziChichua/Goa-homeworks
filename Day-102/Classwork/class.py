#1
def is_vow(inp):
    return [chr(i) if chr(i) in "aeiou" else i for i in inp]

#2
def is_digit(n):
    return len(n) == 1 and n.isdigit()

#3
def distinct(seq):
    res = []
    for i in seq:
        if i not in res:
            res.append(i)
    return res

#7kyu

#1
def printer_error(s):
    errors = sum(1 for i in s if i > "m")
    return f"{errors}/{len(s)}"

#2
def min_max(lst):
    return [min(lst),max(lst)]


#3
def divisors(integer):
    res = [i for i in range(2, integer) if integer % i == 0]
    return res if res else f"{integer} is prime"

#4

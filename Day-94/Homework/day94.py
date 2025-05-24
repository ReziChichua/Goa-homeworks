def remove_smallest(numbers):
    if not numbers:
        return []
    idx = numbers.index(min(numbers))
    return numbers[:idx] + numbers[idx+1:]

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

def get_middle(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 else s[mid-1:mid+1]

def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"

def find_short(s):
    return min(len(word) for word in s.split())

def disemvowel(string):
    return ''.join(c for c in string if c.lower() not in 'aeiou')

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

def maskify(cc):
    return '#' * (len(cc)-4) + cc[-4:] if len(cc) > 4 else cc

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

def is_isogram(string):
    s = string.lower()
    return len(s) == len(set(s))

def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))

def find_average(array):
    return sum(array) / len(array) if array else 0

def make_upper_case(s):
    return s.upper()

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

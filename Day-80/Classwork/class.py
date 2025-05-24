#1
def sum_array(a):
    return sum(a) if a else 0

#2
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


#3
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

#4
def reverse_list(l):
    return l[::-1]


#5
def two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

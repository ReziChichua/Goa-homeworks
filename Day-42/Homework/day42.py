#1
def solution(text, ending):
    return text[-len(ending):] == ending if ending else True

#2
def accum(st):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(st))


#3
def DNA_strand(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna)

#4
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

#5
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
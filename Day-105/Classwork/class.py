#1
def multiply_digits(s):
    result = 1
    for char in s:
        if char.isdigit():
            result *= int(char)
    return result


#2
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split())

#3
def is_isogram(string):
    s = string.lower()
    return len(s) == len(set(s))


#4
def get_count(sentence):
    return sum(1 for char in sentence if char in 'aeiouAEIOU')

#5
def divisors(n):
    return len([i for i in range(1, n + 1) if n % i == 0])


#6
def remove_smallest(numbers):
    n = numbers.copy()
    if numbers == []:
        return []
    else:
        n.remove(min(numbers))
    return n


#1
def in_asc_order(arr):
    return arr == sorted(arr)
        


#2

#3
def flatten_and_sort(array):
    return sorted([num for i in array for num in i])

#4
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


#5
def fizzbuzz(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

#6
def row_weights(array):
    return (sum(array[::2])), sum(array[1::2])

#7
def greet(name): 
    return f"Hello {name.capitalize()}!"

#8
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr)[::-1]:
        return "yes, descending"
    else:
        return "no"
    
#9
def remove_duplicate_words(s):
    words = s.split()
    result = []
    for i in words:
        if i not in result:
            result.append(i)
            
    return " ".join(result)
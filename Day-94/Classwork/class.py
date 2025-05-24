def alphabet_position(text):
    result = []
    for char in text.lower():
        if char.isalpha():
            result.append(str(ord(char) - ord('a') + 1))
    return ' '.join(result)


def bool_to_word(boolean):
    return boolean and "Yes" or "No"


def summation(num):
    x=0
    
    for i in range(1, num + 1):
        x += i
    
    return x

def find_smallest_int(arr):
    return min(arr)
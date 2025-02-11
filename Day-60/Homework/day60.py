#1
def to_alternating_case(string):
    return string.swapcase()

#2
def correct(s):
    corrections = {
        '5': 'S',
        '0': 'O',
        '1': 'I'
    }
    return ''.join(corrections.get(char, char) for char in s)
                   
#3
def bonus_time(salary, bonus):
    total = salary * 10 if bonus else salary
    return f"${total}"

#4
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]


#5
def pig_it(text):
    words = text.split()
    result = []
    
    for word in words:
        if word[-1] in "!?.,;":  
            result.append(word)
        else:
            result.append(word[1:] + word[0] + "ay")  

    return " ".join(result)


#6
def move_zeros(lst):
    non_zeros = [x for x in lst if x != 0] 
    zeros = [0] * (len(lst) - len(non_zeros)) 
    return non_zeros + zeros
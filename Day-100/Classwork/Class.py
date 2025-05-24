#1
def divide_numbers(x, y):
    return x / y

#2
def print_array(arr):
    return ",".join(map(str, arr))

#3
def dating_range(age):
    if age > 14:
        min = age // 2 + 7
        max = 2 * (age - 7)
    else:
        min = int(age - 0.10 * age)
        max = int(age + 0.10 * age)
    return f"{min}-{max}"

#4
def is_opposite(s1,s2):
    if s1 == s2.swapcase():
        return True
    elif s1 == "":
        return False
    else:
        return False
    

#5
def remove(st):
    return st.rstrip('!')

#6
def quote(fighter):
    if fighter.lower() == 'george saint pierre':
        return "I am not impressed by your performance."
    else:
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    
#7
def kata_13_december(lst): 
    return [i for i in lst if i % 2 != 0]


#8
def six_toast(num):
    return abs(num - 6)


#1

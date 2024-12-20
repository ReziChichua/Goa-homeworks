#1
def get_count(sentence):
    count = 0
    for i in sentence:
        if i == "a":
            count += 1
        elif i == "e":
            count += 1
        elif i == "i":
            count += 1
        elif i == "o":
            count += 1
        elif i == "u":
            count += 1
        
    return count

#2
def disemvowel(string_):
    res = ""
    for i in string_:
        if i not in "aeiouAEIOU":
            res += i
    return res

#3
def square_digits(num):
    res = ""
    for i in str(num):
        res += str(int(i)**2)
    return int(res)
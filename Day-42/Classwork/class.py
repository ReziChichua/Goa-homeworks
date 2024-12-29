#1
def is_isogram(string):
    string = string.lower()
    return len(set(string)) == len(string)


#2
def xo(s):
    s = s.lower()

    count_x = s.count('x')
    count_o = s.count('o')

    return count_x == count_o

#3
def to_jaden_case(string): 
    return " ".join(i.capitalize() for i in string.split())

#4
def find_short(s):
    return min(len(word) for word in s.split())
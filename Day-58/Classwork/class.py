#1
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    

#2
def name_shuffler(str_):
    first, last = str_.split()  
    return f"{last} {first}"

#3
def shorten_to_date(long_date):
    return long_date.split(",")[0]

#4
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

#5
def what_century(year):
    return (int(year) + 99) // 100
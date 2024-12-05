#1
def abbrev_name(name):
    first_name, last_name = name.split()
        
    return f"{first_name[0].upper()}.{last_name[0].upper()}"

#2
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    

#3
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    

#4
def find_needle(haystack):
    position = haystack.index("needle")
    return f"found the needle at position {position}"

#5
def invert(lst):
    return [i*-1 for i in lst]
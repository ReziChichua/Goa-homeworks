#1)
def count_sheeps(sheeps):
    count= 0
    for sheep in sheeps:
        if sheep:
            count += 1    
    return count


#2)
def no_space(x):
    return x.replace(' ' ,'')

#3)
def double_integer(i):
    return i*2

#4)
def greet(name):
    return "Hello, " + name + " how are you doing today?"


#5)
def boolean_to_string(b):
    return str(b)
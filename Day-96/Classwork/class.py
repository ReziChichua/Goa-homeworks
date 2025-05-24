#1
def add_length(str_):
    return [f"{i} {len(i)}" for i in str_.split(" ")]

#2
def warn_the_sheep(queue):
    if queue[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    else:
        place = len(queue) - queue.index("wolf") -1
        return f"Oi! Sheep number {place}! You are about to be eaten by a wolf!"
    

#3
def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]

#4
def flip(d, a):
    if d == "R":
        return sorted(a)
    else:
        return sorted(a, reverse=True)
    
#5
def well(x):
    good = x.count("good")
    if good == 0:
        return "Fail!"
    elif good <= 2:
        return "Publish!"
    else:
        return "I smell a series!"
    
#6
def chromosome_check(chromosome):
    xc = chromosome.count("X")
    if xc == 1:
        return "Congratulations! You're going to have a son."
    else:
        return "Congratulations! You're going to have a daughter."
    
#7
def hello(name=""):
    if name == "":
        return "Hello, World!"
    else:
        return f"Hello, {name.capitalize()}!"
    
#8

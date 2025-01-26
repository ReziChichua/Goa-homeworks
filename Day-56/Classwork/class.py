#1
numbs = [10, 50, 9, 64, 19, 90]
ormoczemeti = list(filter(lambda x: x >= 40, numbs))

#2
numbs2 = [1, 2, 3, 4, 5, 6, 7]
squared = list(map(lambda x: x ** 2, numbs2))


#3
str1 = ["data", "apple", "grape", "iphone", "a"]
aa = list(filter(lambda x: x[-1] == "a", str1))


#4
def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name


#5
def move(position, roll):
    return position + roll * 2


#6
def enough(cap, on, wait):
    available_space = cap - on
    if available_space >= wait:
        return 0
    else:
        return wait - available_space
    

#7
def between(a,b):
    return list(range(a, b + 1))

#8
def say_hello(name):
    return "Hello, " + name
lst = [i for i in range(1,101)]
lst2= [i for i in range (1,101,2)]

names = ["Rezi", "Zuka", "Data", "Sergi", "Iralki"]
names1 = ["#" + i.replace("a", "") for i in names]
print(names1)

#Codewars 1
def greet(name):
    if name != "Johnny":
        return "Hello, {name}!".format(name=name)
    elif name == "Johnny":
        return "Hello, my love!"
    
#2
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    else:
        return "green"
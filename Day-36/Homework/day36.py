#1
def rental_car_cost(d):
    daily= 40
    total= daily * d
    if d >= 7:
        return total - 50
    elif d >=3:
        return total - 20
    
    return total

#2
def quarter_of(month):
    return (month - 1) // 3 + 1

#3
def remove_exclamation_marks(s):
    return s.replace("!", "")

#4
def points(games):
    total_points = 0
    for i in games:
        x, y = i.split(":")  
        x, y = int(x), int(y)    
        if x > y:
            total_points += 3  
        elif x == y:
            total_points += 1  
    return total_points

#5
def get_volume_of_cuboid(length, width, height):
    return length * width * height


#manual in keyword
def manual_in(x, y):
    for item in y:
        if item == x:
            return True  
    return False
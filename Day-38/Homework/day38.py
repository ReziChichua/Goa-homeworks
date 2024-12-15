#1
def area_or_perimeter(l , w):
    if l == w :
        return w*l
    else:
        return 2*(w+l)

#2
def other_angle(a, b):
    return 180 - (a+b)

#3
def set_alarm(employed, vacation):
    if employed == vacation:
        return False
    elif employed == True and vacation == False:
        return True
    elif employed == False and vacation == True:
        return False
    
#4
def sum_mix(arr):
    return sum(int(x) for x in arr)

#5
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    x = max(arr)
    y = min(arr)
    arr.remove(x)
    arr.remove(y)
    return sum(arr)


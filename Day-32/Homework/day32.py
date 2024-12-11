#1
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)
    

#2
def smash(words):
    return "".join(words)


#3
def grow(arr):
    count=1
    for i in arr:
        count = count*i
    return count


#4
def hero(bullets, dragons):
    if bullets >= dragons * 2:
        return True
    else:
        return False
    

#5
def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    if your_points > average:
        return True
    else:
        return False
    

def manual_find(s,i):
    y=0
    for x in s:
        if i == x:
            return y
    else:
        y = y + 1
    return -1

def manual_swapcase(s):
    res = ""

    for i in s:
        if i.lower():
            res = res +i.upper()
        else:
            res = res +i.lower()

    return res
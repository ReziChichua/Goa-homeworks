#1
def twice_as_old(dad_years_old, son_years_old):
    x = dad_years_old - 2 * son_years_old
    if x <= 0:
        return -x
    else:
        return x
    
#2
def check_alive(health):
    if health <= 0:
        return False
    else:
        return True
    
#3
def combat(health, damage):
    x = health - damage
    if x < 0:
        return 0
    else:
        return x
    

#4
def how_many_light_sabers_do_you_own(name=None):
    if name == "Zach":
        return 18
    return 0

#5
def amountCheck(arr):
    res = {}
    for i in arr:
        res[i] = res.get(i, 0) + 1
    return res
def find_arr(arr_a, arr_b, rng, wanted):
    res = []
    count_a = amountCheck(arr_a)
    count_b = amountCheck(arr_b)
    for i in range(rng[0],rng[1]+1):
        if count_a.get(i,0) > 1 and count_b.get(i,0) > 1:
            if wanted == "even":
                if i % 2 == 0:
                    res.append(i)
            else:
                if i % 2 != 0:
                    res.append(i)
    return res

#6
def stringy(size):
    return  "".join('1' if i % 2 == 0 else "0" for i in range(size))

#7
def calculator(x, y, op):
    if type(x) == str or type(y) == str:
        return "unknown value"

    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y if y != 0 else "unknown value"
    else:
        return "unknown value"
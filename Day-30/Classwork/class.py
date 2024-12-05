#1
def basic_op(operator, value1, value2):
    if operator == "+" :
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2
    

#2
def litres(time):
    return int(time * 0.5 )


#3
def century(year):
    return (year+99) // 100


#4
def maps(a):
    return [i*2 for i in a]


#5
def digitize(n):
    res=[]
    for i in str(n):
        res.append(int(i))
    return res[::-1]

#1
def fake_bin(x):
    result = ""
    for i in x:
        if int(i) < 5:
            result += "0"
        else:
            result += "1"
    return result

#2
def string_to_array(s):
    return s.split(" ")


#3
def check(seq, elem):
    return elem in seq


#4
def reverse_seq(n):
     return list(range(n, 0, -1))


#5
def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result




#manual_min
def manual_min(arr):
    if arr == "": 
        return "The list is empty"
    minimum = arr[0]  
    for num in arr[1:]:  
        if num < minimum:  
            minimum = num
    return minimum

#manual_max
def manual_max(arr):
    if arr == "": 
        return "The list is empty"
    max = arr[0]  
    for num in arr[1:]:  
        if num > max:  
            max = num
    return max
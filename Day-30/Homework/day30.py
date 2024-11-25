#codewars
#1
def lovefunc( flower1, flower2 ):
    if eval(f"{flower1} + {flower2}") % 2 == 0:
        return False
    else:
        return True
    

#2
def sum_array(a):
    return sum(a)

#3
def paperwork(n, m):
    return n*m if n > 0 and m > 0 else 0

#4
def past(h, m, s):
    return (3600*h + 60*m + s) * 1000


#5
def make_upper_case(s):
    return s.upper()



def manual_len(x):
    count = 0
    for _ in x:
        count += 1
    return count


print(manual_len("hellooo"))
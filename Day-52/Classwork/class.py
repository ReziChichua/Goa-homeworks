#1
def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum


#2
hello = lambda: "Hello world!"


#3
sum1 = lambda x, y: x + y
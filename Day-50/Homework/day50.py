#1
#NameError
try:
    result = not_defined_variable * 2  # NameError: ცვლადი განსაზღვრული არ არის.
except NameError:
    print("NameError: ცვლადი არ არის განსაზღვრული. გთხოვთ, გადაამოწმეთ მისი სახელი.")


#IndexError
lst = ["a", "b", "c"]
try:
    print(lst[10])  # IndexError: ინდექსი არ არსებობს.
except IndexError:
    print("IndexError: სიაში მითითებული ინდექსი არასწორია.")


#ValueError
try:
    num = float("abc")  # ValueError: სტრიქონი რიცხვად ვერ გარდაიქმნება.
except ValueError:
    print("ValueError: მოცემული მნიშვნელობა რიცხვად გარდასაქმნელად არ ვარგა.")


#2
def sum_numbers(numbers):
    valid_numbers = [int(x) for x in numbers if str(x).isdigit()]
    return sum(valid_numbers)



#3
def str_count(strng, letter):
    return strng.count(letter)

#4
def is_even(n): 
    return n % 2 == 0
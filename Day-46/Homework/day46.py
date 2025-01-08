#1
def remove_duplicates(s):
    return ''.join(sorted(set(s)))


#codewars 2
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

#3
def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2)

#4
def get_average(marks):
    return int(sum(marks)// len(marks)) 

#5
def reverse_words(s):
    return ' '.join(s.split()[::-1])

#6
def check_for_factor(base, factor):
    return base % factor == 0
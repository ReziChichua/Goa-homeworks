#1
def longest(a1, a2):
     return ''.join(sorted(set(a1 + a2)))


#2
def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

#3
def find_next_square(sq):
    root = int(sq ** 0.5)
    if root * root == sq:
        return (root + 1) * (root + 1)
    return -1


#4
def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += p0 * (percent / 100) + aug
        years += 1
    return years


#5
def reverse_words(text):
    return " ".join(i[::-1] for i in text.split(" "))
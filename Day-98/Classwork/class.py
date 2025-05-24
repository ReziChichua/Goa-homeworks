#1
def move_zeros(lst):
    no_zeroes = [i for i in lst if i != 0]
    zero = [i for i in lst if i == 0]
    return no_zeroes + zero


#2
def generate_hashtag(s):
    if not s or not s.strip:
        return False
    res = "#" + "".join(i.capitalize() for i in s.strip().split())
    return res if len(res) <=140 else False

#3
def pig_it(text):
    return ' '.join(
        word[1:] + word[0] + 'ay' if word.isalpha() else word
        for word in text.split()
    )

#4
import string

def rot13(message):
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    rotated = string.ascii_uppercase[13:] + string.ascii_uppercase[:13] + \
              string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    translation_table = str.maketrans(alphabet, rotated)
    return message.translate(translation_table)



#5
def dirReduc(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []
    for direction in arr:
        if stack and stack[-1] == opposites[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack

#6
def domain_name(url):
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    if url.startswith("www."):
        url = url[4:]
    return url.split(".")[0]
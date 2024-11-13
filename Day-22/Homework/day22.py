def check_discount(age):
    if age <= 18:
        return "You got discount"
    else:
        return "You didn't get discount"
    
print(check_discount(18))


def manual_reverse(s):
    return s[::-1]

print(manual_reverse("Hello"))

s = "hello world"

# .upper() - ყველა ასო გადადის დიდი ასოებად
print(s.upper())  # "HELLO WORLD"

# .lower() - ყველა ასო გადადის პატარა ასოებად
print(s.lower())  # "hello world"

# .capitalize() - პირველი ასო ხდება დიდი, დანარჩენი პატარა
print(s.capitalize())  # "Hello world"

# .swapcase() - დიდ ასოებს ხდის პატარა და პირიქით
print(s.swapcase())  # "HELLO WORLD"

# .find() - აგრეთვე იძენს სიმბოლოს ინდექსს
print(s.find("world"))  # 6
print(s.find("python"))  # -1 (თუ არ იპოვეს)


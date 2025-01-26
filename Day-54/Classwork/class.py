#1
#Mutable მონაცემთა ტიპები: list, dict, set
#2
#Immutable მონაცემთა ტიპები: int, float, str, tuple
#3
#Lambda ფუნქციას მეორენაირად ეწოდება ანონიმური ფუნქცია 
#4
#map: გამოიყენება ყველა ელემენტზე მოქმედების ჩასატარებლად. filter: გამოიტანს მხოლოდ True ელემენტებს
#5
#ორი სტრინგის შეერთებას ეწოდება კონკატენაცია


#Maps
#1
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
#2
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 32.8, celsius))
#3
words = ["hello", "welcome", "come"]
capitalize = list(map(lambda w: w.capitalize(), words))


#Filters
#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = list(filter(lambda x: x % 2 == 0, numbers))
#2
strings = ["css", "python", "html", "c+"]
long_strings = list(filter(lambda s: len(s) >= 4, strings))
#3
numb = [3, 9, 15, 22, 27, 30]
multiple_three = list(filter(lambda x: x % 3 == 0, numb))
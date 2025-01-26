# 2) 
numbers = [2, 4, 6, 8, 10]
doubled_numbers = list(map(lambda x: x * 2, numbers))


# 3)
names = ["Alice", "Bob", "Charlie"]
greeted_names = list(map(lambda name: "Hello, " + name, names))


# 4) 
strings = ["apple", "banana", "kiwi"]
lengths = list(map(len, strings))


# 5)
numbers_with_negatives = [-5, 3, -2, 7, 0, 10]
positive_numbers = list(filter(lambda x: x > 0, numbers_with_negatives))

# 6)
words = ["pear", "apple", "peach", "grape"]
words_starting_with_p = list(filter(lambda word: word.startswith("p"), words))


# 7) 
random_numbers = [10, 55, 42, 78, 65, 20]
numbers_greater_than_50 = list(filter(lambda x: x > 50, random_numbers))


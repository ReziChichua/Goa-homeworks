for i in range(0, 200, 6):
    print(i)

str1="Hello World"
for i in str1:
    print(i)


for i in range(1000,0,-1):
    print(i)


age = int(input("Enter ur age: "))
if age < 18:
    print("You have a 50%' discount")
else:
    print("No Discount")


age = int(input("Enter ur age: "))
if age < 18:
    print("50% Discount")
elif age == 18:
    print("25% Discount")
else:
    print("Regular Price")


age= int(input("Enter age: "))
is_student = True

if age < 18 or is_student:
    print("50% Discount")
else:
    print("Regular price")
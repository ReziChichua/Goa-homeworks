x=1
for i in range(1,11):
    x *= i
    print(x)


x=1
i=1
while i <=10:
    x *=i
    i+=1
    print(x)


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")


grade = int(input("Enter ur score: "))
if grade >90 <100:
    print("Grade A")
elif grade >80 <90:
    print("Grade B")
elif grade >70 <80:
    print("Grade C")
elif grade >60 <70:
    print("Grade D")
else:
    print("Fail")
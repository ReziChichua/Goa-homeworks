class Car:
    classes_created = 0  #classes variable
    def __init__(self,year, brand, hs_power, weight):
        self.year = year   #instancec variable
        self.klasi = brand
        self.hs_power = hs_power
        self.weight = weight
        Car.classes_created +=1

    def details(self):
        return f"Your car is a {self.brand} its power is {self.hs_power} and it weighs {self.weight}"

    def move (self, action):
        return f"You are {action} your {self.brand}"
    
car1 = Car(1999, "Lamborghini", 10000, "1000kg")
car2= Car(2010, "Toyota", 200, "200kg")
car3 = Car(2025, "Tesla", 500, "500kg")

print(car1.details())    
print(car2.details())
print(car3.detaild())



class Person:
    count = 0  

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        Person.count += 1  

    def get_info(self):
        return f"My name is {self.name} my age is {self.age} I am from {self.city}"
    
    def increase_age(self, years):
        self.age += years
        print(f"{self.name} Your age increased by {years} years.")

person1 = Person("Rezi", 15, "Batumi")
person2 = Person("Data", 25, "Tbilisi")
person3 = Person("Luka", 35, "Kutaisi")




#3
#Dunder Method არის მეთოდი რომელიც სულ იწყება და მთავრდება ორი underscore ით __ 

#4
#Instance variables არის ობიექტზე დამოკიდებული ცვლადები.

#5
#Class variables არის ყველა ობიექტისთვის გაზიარებული ცვლადები.

#6 
#Blueprint არის წინასწარ ჩანახაზი
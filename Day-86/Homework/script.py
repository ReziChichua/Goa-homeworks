#1
#აბსტრაქტული კლასი არის ისეთი კლასი, რომელიც გამოიყენება როგორც "საბაზისო" კლასი და ვერ იქმნება მისგან ობიექტი პირდაპირ.

#2
#პოლიმორფიზმი ნიშნავს ერთნაირი მეთოდის განსხვავებულად განხორციელებას სხვადასხვა კლასში.


#3
#აგრეგაცია არის ორი კლასის ურთიერთობა, სადაც ერთი კლასი შეიცავს მეორე კლასის ობიექტს, მაგრამ არა ისე, რომ დამოკიდებულია მასზე.

#4
from abc import ABC, abstractmethod

class Animal(ABC):  # აბსტრაქტული კლასი
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog()
print(dog.make_sound())  

class Bird:
    def speak(self):
        return "Tweet!"

class Human:
    def speak(self):
        return "Hello!"

def say_something(entity):
    print(entity.speak())

say_something(Bird())   
say_something(Human())  

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine 
engine1 = Engine(120)
car1 = Car("Toyota", engine1)

print(car1.brand)              
print(car1.engine.horsepower)  
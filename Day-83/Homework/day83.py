#1
class Motorcycle:
    total_motorcycles = 0  

    def __init__(self, brand, model, engine_capacity, color):
        self.brand = brand
        self.model = model
        self.engine_capacity = engine_capacity
        self.color = color
        Motorcycle.total_motorcycles += 1

    def get_info(self):
        return f"{self.brand} {self.model}, Engine: {self.engine_capacity}cc, Color: {self.color}"


moto1 = Motorcycle("Yamaha", "R1", 1000, "Blue")
moto2 = Motorcycle("Honda", "CBR600RR", 600, "Red")
moto3 = Motorcycle("Ducati", "Panigale V4", 1100, "Black")

# Testing attributes and method
print(moto1.get_info())
print(moto2.get_info())
print(moto3.get_info())

print(f"Total motorcycles created: {Motorcycle.total_motorcycles}")


#2
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Unknown sound"

# Child classes (Inheritance)
class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Bird(Animal):
    def make_sound(self):
        return "Chirp"


dog = Dog("Bella", "Dog")
cat = Cat("Milo", "Cat")
bird = Bird("Chirpy", "Sparrow")

# Displaying their sounds
print(f"{dog.name}: {dog.make_sound()}")
print(f"{cat.name}: {cat.make_sound()}")
print(f"{bird.name}: {bird.make_sound()}")


#3
class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("The car is driving")

car = Car()
car.move() 


#4
#So We don’t need to rewrite the same methods in multiple classes.

#5
class Engine:
    def start(self):
        print("Engine started")

class Wheels:
    def rotate(self):
        print("Wheels are rotating")

class Car(Engine, Wheels):
    def drive(self):
        print("Car is driving")

car = Car()
car.start()  
car.rotate()  
car.drive() 
from abc import ABC, abstractmethod

class Animal(ABC):  # ABC ნიშნავს, რომ ეს არის აბსტრაქტული კლასი
    @abstractmethod
    def make_sound(self):
        pass  # არ აქვს განხორციელება

class Dog(Animal):
    def make_sound(self):
        return "Bark"

dog = Dog()
print(dog.make_sound())



class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    def sound(self):
        return "Quack!"


class Human:
    def speak(self):
        return "I can speak."

class Student(Human):
    def study(self):
        return "I am studying."

class UniversityStudent(Student):
    def research(self):
        return "I do research."

#კომპოზიცია (Composition):
#ეს არის როცა ერთ ობიექტში მთლიანად „შენახულია“ სხვა ობიექტი.
#თუ მშობელი ობიექტი განადგურდება, მასთან ერთად შვილობილი ობიექტიც განადგურდება.


#აგრეგაცია (Aggregation):
#ობიექტები loosely დაკავშირებულნი არიან.
#შვილობილი ობიექტი ცალკე ცხოვრობს, მშობელ ობიექტთან ერთად გამოიყენება, მაგრამ მისი არსებობა მისზე არ არის დამოკიდებული.



# Composition
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  

    def start(self):
        self.engine.start()

car = Car()
car.start()  

#2
class MathDemo:
    factor = 10

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        return self.value * 2

    @staticmethod
    def static_method(x, y):
        return x + y

    @classmethod
    def class_method(cls, x):
        return x * cls.factor


#3
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
print(duck.fly())   # Flying
print(duck.swim())  # Swimming


#4
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  

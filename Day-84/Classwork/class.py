class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        return f"Hello, my name is {self.name} and i am {self.age} years old"
    

class Programmer(human):
    def code(self):
        return f"{self.name} is doing codewars"
    
class Designer(human):
    def design(self):
        return f"{self.name} is designing a website"
    

class GoaProgrammer(Programmer):
    def gitcode(self):
        return f"{self.name} is uploading his codewars on github"
    
class GoaDesigner(Designer):
    def gitdesign(self):
        return f"{self.name} is uploading his frontendmentor on github"
    
class Professional (Programmer, Designer):
    def makemoney(self):
        return f"{self.name} is teaching others and making money with his codes"
    

goa_programmer = GoaProgrammer("Data", 15)
goa_designer = GoaDesigner("Rezi", 18)
professional = Professional("Luka", 50)


print(professional.makemoney())
print(goa_programmer.intro())
print(goa_designer.design())


#2
#super() ფუნქცია გამოიყენება, parent კლასის მეთოდებისა და ატრიბუტების გამოსაძახებლად child კლასში.

#3
#როდესაც super() გამოვიძახებთ child კლასში,
#  ის მიმართავს parent კლასს და გვაძლევს საშუალებას გამოვიყენოთ მისი მეთოდები და ატრიბუტები


#4
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def vehicle_info(self):
        return f"Vehicle: {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model) 
        self.doors = doors  

    def car_info(self):
        return f"{super().vehicle_info()}, Doors: {self.doors}"

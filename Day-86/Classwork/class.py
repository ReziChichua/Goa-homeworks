from abc import ABC, abstractmethod

#1
class Gamble(ABC):
    @abstractmethod
    def Spin_The_Wheel(self):
        pass  


class Winner(Gamble):
    def Spin_The_Wheel(self):
        return "Jackpot"

class Loser(Gamble):
    def Spin_The_Wheel(self):
        return "Lose Everything"
    

#2

class Bird:
    def make_sound(self):
        return "Chirp"

class Cow:
    def make_sound(self):
        return "Moo"

class Snake:
    def make_sound(self):
        return "Hiss"
    

#3
#Polymorphism - პოლიმორფიზმი ნიშნავს: ერთი და იგივე მეთოდის სხვადასხვა ქცევა სხვადასხვა კლასში
#Abstract - გვაიძულებს, შვილობილმა კლასებმა შექმნან კონკრეტული მეთოდები.


#4
class Book:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, book):
        self.books.append(book)  

    def show_books(self):
        print("Library contains:")
        for book in self.books:
            print(f"- {book.get_title()}")


book1 = Book("Titanic")
book2 = Book("Vefxvistyaosani")

my_library = Library()

my_library.add_book(book1)
my_library.add_book(book2)
my_library.show_books()
//1
let myObject = {name: 'Alice', age: 30};

//2
function Person(name, age) {
    this.name = name;
    this.age = age;
    this.greet = function() {
      console.log(`გამარჯობა, მე ვარ ${this.name} და მე ${this.age} წლის ვარ.`);
    };
  }

//3
/*ფუნქცია:

დამოუკიდებელი ფუნქცია, რომელიც არ არის დაკავშირებული კონკრეტულ ობიექტთან ან კლასთან.
შეიძლება იყოს პარამეტრები და დაბრუნდეს მნიშვნელობა.
შეიძლება იყოს გამოძახებული პირდაპირ მისი სახელით.
მეთოდი:

ფუნქცია, რომელიც დაკავშირებულია კონკრეტულ კლასთან ან ობიექტთან.
მეთოდებს აქვთ წვდომა კლასის ან ობიექტის თვისებებზე.
მეთოდები გამოძახებულია ობიექტის ან კლასის საშუალებით.*/



//4
function Person(name, age, gender) {
    this.name = name;
    this.age = age;
    this.gender = gender;
  }

//5
function Car(make, model, year, horsePower) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.horsePower = horsePower;
    this.increaseHorsePower = function() {
      this.horsePower += 100;
    };
  }



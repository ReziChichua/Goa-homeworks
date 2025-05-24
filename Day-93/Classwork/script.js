//1
class Animal {
    constructor (name) {
        this.name = name
    }
    speak() {
      return "The animal is speaking . . ."
    }
  }
class Dog extends Animal {
    speak() {
      return "Bark"; 
    }
  }
  

const genericAnimal = new Animal();
genericAnimal.speak();
  
const dog = new Dog();
dog.speak(); 


//2
class User {
    static count = 0; 

    constructor(name) {
      this.name = name;
      User.count++;
    }
  
    static getUserCount() {
      return User.count;
    }
  }


//3

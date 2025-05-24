class Car {
    constructor(make, model) {
      this.make = make;
      this.model = model;
    }
  }
  
  const car1 = new Car("Toyota", "Corolla");
  console.log(car1.make);  // Toyota
  console.log(car1.model); // Corolla

  

  class BankAccount {
    #balance;
  
    constructor(initialBalance) {
      this.#balance = initialBalance;
    }
  
    deposit(amount) {
      this.#balance += amount;
    }
  
    withdraw(amount) {
      if (amount <= this.#balance) {
        this.#balance -= amount;
      } else {
        console.log("Insufficient funds.");
      }
    }
  
    getBalance() {
      return this.#balance;
    }
  }
  
  const account = new BankAccount(100);
  account.deposit(50);
  account.withdraw(30);
  console.log(account.getBalance()); // 120

  
  class MathOperations {
    static PI = 3.14159;
  
    static add(a, b) {
      return a + b;
    }
  }
  
  console.log(MathOperations.add(4, 5)); // 9
  console.log(MathOperations.PI);       // 3.14159

  

  class Rectangle {
    constructor(width, height) {
      this._width = width;
      this._height = height;
    }
  
    get area() {
      return this._width * this._height;
    }
  
    set width(value) {
      if (value > 0) this._width = value;
    }
  
    set height(value) {
      if (value > 0) this._height = value;
    }
  }
  
  const rect = new Rectangle(5, 10);
  console.log(rect.area); 
  rect.width = -4; 
  console.log(rect.area); 
  

  class User {
    #password;
  
    constructor(name) {
      this.name = name;
    }
  
    setPassword(password) {
      if (this.#validatePassword(password)) {
        this.#password = password;
        console.log("Password set.");
      } else {
        console.log("Weak password.");
      }
    }
  
    #validatePassword(password) {
      return password.length >= 6;
    }
  }
  
  const user1 = new User("Nika");
  user1.setPassword("123");     // Weak password.
  user1.setPassword("123456");  // Password set.
  
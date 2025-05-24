class Author {
    constructor(name) {
      this.name = name;
    }
  }
  
  class Book {
    constructor(title, author) {
      this.title = title;
      this.author = author; 
    }
  
    displayInfo() {
      console.log(`წიგნი: ${this.title}, ავტორი: ${this.author.name}`);
    }
  }


class Employee {
  #salary; 
  
  constructor(name, salary) {
    this.name = name;
    this.#salary = salary;
  }

  getSalary() {
    return this.#salary;
  }
}

class Manager extends Employee {
  constructor(name, salary, department) {
    super(name, salary);
    this.department = department;
  }

  displayInfo() {
    console.log(`სახელი: ${this.name}, განყოფილება: ${this.department}, ხელფასი: ${this.getSalary()}`);
  }
}


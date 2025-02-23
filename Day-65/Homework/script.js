function Book(title, author, genre, yearPublished, pageCount) {
    this.title = title;
    this.author = author;
    this.genre = genre;
    this.yearPublished = yearPublished;
    this.pageCount = pageCount;
  }
  

  const book1 = new Book("მისტერიების სახლი", "ჯონ დოე", "დეტექტივი", 2021, 320);
  console.log(book1);


function Motorcycle(brand, model, engineCapacity, color) {
    this.brand = brand;
    this.model = model;
    this.engineCapacity = engineCapacity;
    this.color = color;
  
    this.startEngine = function() {
      console.log(`${this.brand} ${this.model}-ის ძრავა ჩაირთო!`);
    };
  }


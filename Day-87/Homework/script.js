// 1
function sum(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
  }
  console.log(sum(1, 2, 3, 4)); // 10
  
  
  const user = { name: "Ana", age: 23, city: "Tbilisi" };
  const { name, ...rest } = user;
  console.log(name); // Ana
  console.log(rest); // { age: 23, city: "Tbilisi" }
  


// 2
const a = [1, 2];
const b = [3, 4];
const result = [...a, ...b];
console.log(result); // [1, 2, 3, 4]


//3
function multiply(multiplier, ...nums) {
    return nums.map(n => n * multiplier);
  }
  
  const numbers = [1, 2, 3];
  const res = multiply(2, ...numbers); 
  console.log(result); // [2, 4, 6]



//4
//localStorage არის ბრაუზერის შიდა მეხსიერება, სადაც შეგვიძლია მონაცემების შენახვა კლავიშების წყვილის (key-value) სახით.


  
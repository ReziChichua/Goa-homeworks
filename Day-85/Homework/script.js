const numbers = [10, 20, 30, 40, 50];

// Destructuring
const [a, b, c, d, e] = numbers;


const user = {
    name: "Nika",
    age: 25,
    city: "Tbilisi"
  };
  
  // Destructuring
  const { name, age, city } = user;
  
  console.log(name); 
  console.log(age)
  console.log(city);


  const arr1 = [1, 2, 3];
  const arr2 = [...arr1, 4, 5];
  console.log(arr2);
  
 
  const [first, ...rest] = [10, 20, 30, 40];
  console.log(first);
  console.log(rest);


  function sum(...nums) {
    return nums.reduce((total, n) => total + n, 0);
  }
  
  console.log(sum(1, 2));            
  console.log(sum(5, 10, 15));        
  console.log(sum(100, 200, 300, 10));

  const original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const copy = [...original];
  
  console.log(copy); 



  const person = {
    name: "Lika",
    age: 22,
    city: "Kutaisi",
    country: "Georgia",
    profession: "Designer"
  };
  

  const { name1, age1, ...restInfo } = person;
  
  console.log(name1);      
  console.log(age1);       
  console.log(restInfo);
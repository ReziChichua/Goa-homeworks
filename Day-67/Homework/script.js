function sumArray(numbers) {
    return numbers.reduce((sum, num) => sum + num, 0);
  }
  console.log(sumArray([5, 10, 15]));

function minMaxArray(numbers) {
    return {
      min: Math.min(...numbers),
      max: Math.max(...numbers)
    };
  }
console.log(minMaxArray([5, 10, 2, 25, 8]))


function generateRandomArray(n) {
    const randomArray = [];
    for (let i = 0; i < n; i++) {
      randomArray.push(Math.floor(Math.random() * 100) + 1);
    }
    return randomArray;
  }
  console.log(generateRandomArray(5)); 


function squareArray(numbers) {
    return numbers.map(num => num ** 2);
  }
  console.log(squareArray([2, 3, 4]));


  function roundNumber(num) {
    return {
      floor: Math.floor(num),
      ceil: Math.ceil(num),
      round: Math.round(num)
    };
  }
  console.log(roundNumber(4.7));  
// 1. Multiply
function multiply(a, b) {
  return a * b;
}

// 2. Convert boolean values to strings 'Yes' or 'No'.
function boolToWord(bool) {
  return bool ? 'Yes' : 'No';
}

// 3. Even or Odd
function evenOrOdd(number) {
  return number % 2 === 0 ? 'Even' : 'Odd';
}

// 4. Return Negative
function makeNegative(num) {
  return num > 0 ? -num : num;
}

// 5. String repeat
function repeatStr(n, s) {
  return s.repeat(n);
}

// 6. Remove First and Last Character
function removeChar(str) {
  return str.slice(1, -1);
}

// 7. Sum of positive
function positiveSum(arr) {
  return arr.filter(x => x > 0).reduce((sum, x) => sum + x, 0);
}

// 8. Opposite number
function opposite(number) {
  return -number;
}

// 9. Basic Mathematical Operations
function basicOp(operation, value1, value2) {
  switch(operation){
    case '+': return value1 + value2;
    case '-': return value1 - value2;
    case '*': return value1 * value2;
    case '/': return value1 / value2;
  }
}

// 10. Reversed Strings
function solution(str) {
  return str.split('').reverse().join('');
}

// 11. Convert number to reversed array of digits
function digitize(n) {
  return n.toString().split('').reverse().map(Number);
}

// 12. Find the smallest integer in the array
class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min(...args);
  }
}

// 13. Sum Arrays
function sum(numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}

// 14. You only need one - Beginner
function check(a, x) {
  return a.includes(x);
}

// 15. Is n divisible by x and y?
function isDivisible(n, x, y) {
  return n % x === 0 && n % y === 0;
}

// 16. Invert values
function invert(array) {
  return array.map(x => -x);
}

// 17. Find Maximum and Minimum Values of a List
var min = function(list){
  return Math.min(...list);
}

var max = function(list){
  return Math.max(...list);
}

// 18. Remove String Spaces
function noSpace(x) {
  return x.replace(/\s/g, '');
}

// 19. Count of positives / sum of negatives
function countPositivesSumNegatives(input) {
  if (!input || input.length === 0) return [];
  let count = 0, sum = 0;
  input.forEach(n => n > 0 ? count++ : sum += n);
  return [count, sum];
}

// 20. Counting sheep...
function countSheeps(arrayOfSheep) {
  return arrayOfSheep.filter(Boolean).length;
}

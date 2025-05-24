function add(a, b) {
    return a + b;
  }
  
  function subtract(a, b) {
    return a - b;
  }
  
  module.exports = { add, subtract };

  
export function multiply(a, b) {
  return a * b;
}

export function divide(a, b) {
  return a / b;
}

export default function greet(name) {
  return `Hello, ${name}!`;
}

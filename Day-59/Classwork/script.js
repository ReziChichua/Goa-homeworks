let num1 = Number(prompt("Enter your first number:"))
let num2 = Number(prompt("Enter your second nummer"))
let sum = num1 + num2

console.log(sum)

let name = prompt("Enter your name")
console.log("Hello!," + name)

document.getElementById("nameForm").addEventListener("submit", function(event) {
    event.preventDefault()})
    
let userName = document.getElementById("name1").value;
console.log(userName);
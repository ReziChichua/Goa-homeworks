//1
let elements = document.getElementsByClassName("my-class");

//2
let elementById = document.querySelector("#my-id");
console.log(elementById);


let elementByClass = document.querySelector(".my-class");
console.log(elementByClass);


//3
let img = document.querySelector("img");
img.src = "new-image.jpg";
img.width = 300;

//4
let paragraph = document.querySelector("p");
paragraph.style.color = "red"; 
paragraph.style.backgroundColor = "yellow"; 
paragraph.style.fontSize = "20px";


//5
let newParagraph = document.createElement("p");
let textNode = document.createTextNode("NewText")
div.appendChild(newParagraph); 
// 1
let score = prompt("Enter your score (0-100):");

if (score >= 90 && score <= 100) {
    alert("Grade A");
} else if (score >= 80 && score <= 89) {
    alert("Grade B");
} else if (score >= 70 && score <= 79) {
    alert("Grade C");
} else if (score >= 60 && score <= 69) {
    alert("Grade D");
} else if (score >= 0 && score <= 59) {
    alert("Grade F");
} else {
    alert("No Score");
}

// 2
let age = prompt("Enter your age:");

if (age < 13) {
    alert("You are kid");
} else if (age < 18) {
    alert("You are not adult yet");
} else {
    alert("You are adult");
}


//4
let num = 0;
while (num <= 100) {
    console.log(num);
    num++;
}

//5

for (let x = 5; x <= 100; x++) {
    console.log(i);
}
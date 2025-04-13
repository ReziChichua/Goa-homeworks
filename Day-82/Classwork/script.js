let user = {
    firstName: "Rezi",
    lastName: "Chichua",
    age: 15
};

localStorage.setItem("userData", JSON.stringify(user));


let retrievedUser = JSON.parse(localStorage.getItem("userData"));

console.log("Age:", retrievedUser.age);

retrievedUser.firstName = "Data";

localStorage.setItem("userData", JSON.stringify(retrievedUser));

let updatedUser = JSON.parse(localStorage.getItem("userData"));
console.log("Updated Name:", updatedUser.firstName);
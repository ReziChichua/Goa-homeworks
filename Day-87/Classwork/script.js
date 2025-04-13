let counter = localStorage.getItem("personCount")
      ? parseInt(localStorage.getItem("personCount"))
      : 0;

document.getElementById("userForm").addEventListener("submit", function (e) {
      e.preventDefault();

const name = document.getElementById("name").value;
const email = document.getElementById("email").value;
const age = document.getElementById("age").value;

      const person = {
        name,
        email,
        age,
      };

      counter++;
      localStorage.setItem(`person${counter}`, JSON.stringify(person));
      localStorage.setItem("personCount", counter); 
     
      document.getElementById("userForm").reset();

      alert(`Person ${counter} saved!`);
    });



document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("signup-form");

    form.addEventListener("submit", function (event) {
      event.preventDefault(); 

      
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const interests = document.getElementById("interests").value;

      
        localStorage.setItem("name", name);
        localStorage.setItem("email", email);
        localStorage.setItem("interests", interests);

      
      alert("Your data has been saved!");
    });
  });


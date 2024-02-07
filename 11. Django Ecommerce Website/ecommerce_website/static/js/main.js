const toggleButton = document.getElementById('toggler');
const navigationLinks = document.getElementById('navbar-links');
const navbar = document.querySelector('.navbar-mobile');

toggleButton.addEventListener('click', () => {
    navigationLinks.classList.toggle('show');
    navbar.classList.add('border');

    if (navigationLinks.classList.contains('show')) {
        toggleButton.innerHTML = '&times;'; // Change to times symbol
    } else {
        toggleButton.innerHTML = '&#8801;'; // Change back to menu symbol
    }
});


const loginFormButton = document.getElementById("login-button");
const signinForm = document.getElementById("signin-form");
const closeModal = document.getElementById("close");
const cancel = document.getElementById("cancelbtn");


loginFormButton.addEventListener("click", () => {
    signinForm.style.display = "block";
})

closeModal.addEventListener("click", () => {
    signinForm.style.display = "none";
})

cancel.addEventListener("click", () => {
    signinForm.style.display = "none";
})

// Registration form
const signupFormButton = document.getElementById("signup-button");
const signupForm = document.getElementById("signup-form");
const closeSignupForm = document.getElementById("close-signup-form");
const cancelSignup = document.getElementById("cancel-signup-button");

signupFormButton.addEventListener("click", () => {
    signupForm.style.display = "block";
})

closeSignupForm.addEventListener("click", () => {
    signupForm.style.display = "none";
})

cancelSignup.addEventListener("click", () => {
    signupForm.style.display = "none";
})

// close the login and signup form when a user clicks outside the forms
// window.onclick = (event) =>{
//     if (event.target == signupForm || event.target == signinForm) {
//         signupForm.style.display = "none";
//         signinForm.style.display = "none";
//     }
// }

// Footer

const currentYear = document.getElementById('current-year');

let date = new Date();
let newDate = date.getFullYear();

currentYear.innerHTML = newDate;




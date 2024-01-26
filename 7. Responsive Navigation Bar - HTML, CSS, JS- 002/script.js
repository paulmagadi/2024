const toggleButton = document.getElementById('toggler');
const navigationLinks = document.getElementById('navbar-links');
const navbar = document.querySelector('.navbar-mobile');

toggleButton.addEventListener('click', () => {
    navigationLinks.classList.toggle('show');
    navbar.classList.add('border');
});






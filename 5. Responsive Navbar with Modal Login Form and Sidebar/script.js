function showNavbar(){
    const sidebar = document.querySelector('.navbar')
    sidebar.style.display = 'flex';
}

function hideNavbar(){
    const sidebar = document.querySelector('.navbar')
    sidebar.style.display = 'none';
}




const sidebar = document.querySelector('.side-bar');
const toggleButton = document.querySelector('.toggle-button');

toggleButton.addEventListener('click', () => {
    sidebar.classList.toggle('show');

// Change button content based on sidebar visibility
    if (sidebar.classList.contains('show')) {
        toggleButton.innerHTML = '&times;'; // Change to times symbol
    } else {
        toggleButton.innerHTML = '&#8801;'; // Change back to menu symbol
    }
});
  



const loginFormBtnMobile = document.getElementById("login-form-mobile");
const loginFormBtn = document.getElementById("login-form");
const modal = document.getElementById("modal");
const closeModal = document.getElementById("close");
const cancel = document.getElementById("cancelbtn");

// loginFormBtn.addEventListener("click", function(){
//     modal.style.display = "block";
// })

loginFormBtnMobile.addEventListener("click", () => {
    modal.style.display = "block";
})

loginFormBtn.addEventListener("click", () => {
    modal.style.display = "block";
})

closeModal.addEventListener("click", () => {
    modal.style.display = "none";
})

cancel.addEventListener("click", () => {
    modal.style.display = "none";
})

// close the modal form when a user clicks outside the modal

window.onclick = (event) =>{
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
    
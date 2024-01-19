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
  
    
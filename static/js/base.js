searchForm = document.querySelector('.search-form');
document.querySelector('#search-btn').onclick =() => {
    searchForm.classList.toggle('active');
}


document.addEventListener("DOMContentLoaded", function() {
  let loginForm = document.querySelector('.login-form-container');
 
  document.querySelector("#login-btn").addEventListener("click", function() {
    loginForm.classList.toggle('active');
  });

});

var closeBtn = document.getElementById('close-login-btn');
closeBtn.addEventListener('click', closeLoginPage);

function closeLoginPage() {
  var loginPage = document.querySelector('.login-form-container');
  loginPage.style.display = 'none';
  
  // Redirect to home.html
  window.location.href = '/';
}
// Get the cancel button element
const cancelButton = document.querySelector('.cancel-button');

// Add a click event listener to the cancel button
cancelButton.addEventListener('click', function(event) {
  event.preventDefault(); // Prevent the default form submission behavior
  // Hide or remove the logout form from the page
  const logoutForm = document.querySelector('.logout-form');
  logoutForm.style.display = 'none'; // or logoutForm.remove();
  
});
// sing-up-form
const signUpForm = document.querySelector('.sign-up-form');

  // Add event listener for the keydown event
  document.addEventListener('keydown', function (event) {
    // Check if the pressed key is the "Escape" key
    if (event.key === 'Escape') {
      // Toggle the visibility of the sign-up form
      signUpForm.classList.toggle('hidden');
    }
});
window.onscroll = () => {

    searchForm.classList.remove('active');

    if (window.scrollY > 80) {
        
        document.querySelector('.header .header-2').classList.add('active');
    } else {
        document.querySelector('.header .header-2').classList.remove('active');
    }
}

window.onload = () => {
    
    if (window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    } else {
        document.querySelector('.header .header-2').classList.remove('active');
    }
}
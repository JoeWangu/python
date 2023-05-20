document.getElementById('asignup').addEventListener('click', register);
document.getElementById('alogin').addEventListener('click', login);
var login = document.getElementById('login');
var register = document.getElementById('register');


function login() {
    login.style.display = 'flex';
    register.style.display = 'none';
}

function register() {
    login.style.display = 'none';
    register.style.display = 'flex'
}
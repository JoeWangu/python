// // ----------------------------------------------------------------------------------------------------------------------
// // ---------------------------------------------------- ADDING THE EYE ICON TO THE PASSWORD INPUTS ----------------------
// // ----------------------------------------------------------------------------------------------------------------------
// const password1 = document.getElementById("id_password1");
// const password2 = document.getElementById("id_password2");
// // const password = document.querySelector(".password-input")

// const icon1 = document.createElement("i");
// const icon2 = document.createElement("i");

// const parent1 = password1.parentElement;
// const parent2 = password2.parentElement;

// icon1.classList.add("fa-regular", "fa-eye");
// icon2.classList.add("fa-regular", "fa-eye");

// // <i class="fa-regular fa-eye-slash"></i>
// // <i class="fa-regular fa-eye"></i>

// parent1.insertBefore(icon1, password1.nextElementSibling)
// parent2.insertBefore(icon2, password2.nextElementSibling)

// // ----------------------------------------------------------------------------------------------------------------------
// // ---------------------------------------------------------- MANIPULATING THE EYE ICONS --------------------------------
// // ----------------------------------------------------------------------------------------------------------------------

// icon1.addEventListener("click", seeAndHidePassword1)
// icon2.addEventListener("click", seeAndHidePassword2)

// function seeAndHidePassword1() {
//     if (password1.type == 'password') {
//         password1.type = 'text'
//         icon1.classList.replace("fa-eye", "fa-eye-slash")
//     } else {
//         password1.type = 'password'
//         icon1.classList.replace("fa-eye-slash", "fa-eye")
//     }
// }

// function seeAndHidePassword2() {
//     if (password2.type == 'password') {
//         password2.type = 'text'
//         icon2.classList.replace("fa-eye", "fa-eye-slash")
//     } else {
//         password2.type = 'password'
//         icon2.classList.replace("fa-eye-slash", "fa-eye")
//     }
// }

const passwordInputs = document.querySelectorAll('[type="password"]');
// const icons = [];

passwordInputs.forEach((input) => {
    const icon = document.createElement("i");
    icon.classList.add("fa-regular", "fa-eye");
    input.parentElement.insertBefore(icon, input.nextElementSibling);
    // icons.push(icon);
    icon.addEventListener("click", togglePasswordVisibility);
});

function togglePasswordVisibility(event) {
    const input = event.target.previousElementSibling;
    if (input.type === "password") {
        input.type = "text";
        event.target.classList.replace("fa-eye", "fa-eye-slash");
    } else {
        input.type = "password";
        event.target.classList.replace("fa-eye-slash", "fa-eye");
    }
}
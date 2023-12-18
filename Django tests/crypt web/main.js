let slideIndex = 1;
showSlides(slideIndex);

let intervalId = setInterval(function () { plusSlides(1) }, 3000);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName('mySlides');
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = 'none';
    }
    slides[slideIndex - 1].style.display = 'flex';

    let dots = document.getElementsByClassName('dot');
    for (i = 0; i < dots.length; i++) {
        dots[i].classList.remove('active')
    }
    dots[slideIndex - 1].classList.add('active');
}

let slideshowContainer = document.getElementsByClassName("image")[0];
slideshowContainer.addEventListener("mouseover", stopSlideshow);
slideshowContainer.addEventListener("mouseout", startSlideshow);

function stopSlideshow() {
    clearInterval(intervalId);
}

function startSlideshow() {
    intervalId = setInterval(function () { plusSlides(1) }, 3000);
}

var navbar = document.getElementById('nav');
// toggle buttons
function toggle() {
    if (navbar.style.display == 'flex') {
        navbar.style.display = 'none';
    } else {
        navbar.style.display = 'flex';
    }
}

function handleResize() {
    var screenWidth = window.innerWidth || document.documentElement.clientWidth;
    if (screenWidth > 640) {
        navbar.style.display = 'flex';
    }
}

window.addEventListener('resize', handleResize);
let currentSlide = 0;

function prevSlide() {
    currentSlide = (currentSlide - 1 + 5) % 5;
    updateCarousel();
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % 5;
    updateCarousel();
}

function updateCarousel() {
    const carousel = document.getElementById('carousel');
    const offset = -currentSlide * 340; // Adjust the value based on the card width and gap
    carousel.style.transform = `translateX(${offset}px)`;
}

document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.querySelector('.nav__toggle');
    const navItems = document.querySelector('.nav__items');

    toggleButton.addEventListener('click', function () {
        navItems.classList.toggle('show');
        toggleButton.classList.toggle('open');
    });
});

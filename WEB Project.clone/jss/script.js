// Toggle class active hamburger menu

const navbarNav = document.querySelector(' .navbar-nav');

// ketika humburger menu di click
document.querySelector('#hamburger-menu').
onclick = (e) => {
navbarNav.classList.toggle('active');
e.preventDefault();
};

//Toggle class active shoping cart
const shoppingCart = document.querySelector('.shopping-cart');

document.querySelector('#shopping-cart-button').onclick = (e) => {
    shoppingCart.classList.toggle('active');
    e.preventDefault();
}


// Toggle class active untuk search form
const searchForm = document.querySelector('.search-form');
const searchBox = document.querySelector('#search-box');

document.querySelector('#search').onclick = (e) => {
    searchForm.classList.toggle('active');
    searchBox.focus();
    e.preventDefault();
};

// klik di luar sidebar untuk menghilangkan nav dan search box

const hm = document.querySelector('#hamburger-menu');
const sb = document.querySelector("#search");
const sc = document.querySelector('#shopping-cart-button');

document.addEventListener('click', function(e) {
    if(!hm.contains(e.target) && !navbarNav.contains(e.target)) {
        navbarNav.classList.remove('active');
    }

    if(!sb.contains(e.target) && !searchForm.contains(e.target)) {
        searchForm.classList.remove("active");
    }

    if(!sc.contains(e.target) && !shoppingCart.contains(e.target)) {
        shoppingCart.classList.remove('active');
    }
});



//Modal Box

// Click outside to close modal
window.onclick = (e) => {
    const modal = document.querySelector('#item-detail-modal');
    if (e.target === modal) {
        Alpine.store('modal').close();
    }
};
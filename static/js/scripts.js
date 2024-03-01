document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.querySelector('.btn-outline-dark');
    const productNameInput = document.querySelector('input[name="product_name"]');

    searchButton.addEventListener('click', function(event) {
        productNameInput.value = ''; // Input qiymatini tozalash
    });
});

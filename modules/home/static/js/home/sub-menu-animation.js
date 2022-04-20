const transactionOptions = document.getElementById("menu-body__option-transaction");

function toggleMenu() {
    const transactionSubOptions = document.getElementById("option-transaction__suboption");
    const transactionArrowIcon = document.getElementById("option-transaction__arrow");

    transactionSubOptions.classList.toggle('sub-options-activate');
    transactionArrowIcon.classList.toggle('arrow-sub-options-activate');
}

transactionOptions.addEventListener('click', toggleMenu);
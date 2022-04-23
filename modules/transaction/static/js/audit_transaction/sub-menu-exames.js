const optionExam = document.getElementById("body__option-exam");

function toggleMenu() {

    const subOptionExam = document.getElementById("option-exam__sub-option-exam");
    const examArrow = document.getElementById("option-exam__arrow");

    subOptionExam.classList.toggle('sub-option--enable');
    examArrow.classList.toggle('option-exam__arrow--rotate');
}

optionExam.addEventListener('click', toggleMenu);
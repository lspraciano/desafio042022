

(() => {

    const iconMenu = document.getElementById("navigation-zone__menu-icon");
    const sideZone = document.getElementById("side-zone");

    function hiddendSideZone() {

        sideZone.classList.toggle('side-zone--disable');
    }

    iconMenu.addEventListener('click', hiddendSideZone);

}) ()
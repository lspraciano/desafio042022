const iconMenu = document.getElementById("navigation-zone_menu-icon");


function showAndHideMenuZone() {
    const menuZone = document.getElementById("side-bar-zone");

    menuZone.classList.toggle('side-bar-zone--hide');
}

iconMenu.addEventListener('click', showAndHideMenuZone);
import {deleteCookie} from "../../../../../resources/js/cookie/cookie-manager.js";


const btnLogout = document.getElementById("logout__btn");
const iconLogout = document.getElementById("logout__icon");

(() => {


    const logout = async () => {
        await deleteCookie();
        window.location.href = `${window.location.origin}/`;
    }

    btnLogout.addEventListener('click', logout);
    iconLogout.addEventListener('click', logout);

})();


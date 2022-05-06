import {hideTableShowForm} from "./show-and-hide-table-form.js";


const newUserButton = document.getElementById("search__button-new-user");


const showForm = () => {
    hideTableShowForm();
}


newUserButton.addEventListener('click', showForm)
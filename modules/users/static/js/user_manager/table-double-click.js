import {hideTableShowForm} from "./show-and-hide-table-form.js";
import {loadDataOnForm} from "./form-data-controller.js";

( () => {

    const tableBody = document.getElementById("table-users__body");

    tableBody.addEventListener("dblclick",  (e) => {
        const userValuesList = [];
        const selectedRow = e.target.parentElement;

        for (let cell of selectedRow.cells) {
            userValuesList.push(cell.innerText);
        }

        let userName = userValuesList[1];
        let userEmail = userValuesList[2];
        let userStatus = userValuesList[3];

        hideTableShowForm();
        loadDataOnForm(userName, userEmail, userStatus);

    });

})();
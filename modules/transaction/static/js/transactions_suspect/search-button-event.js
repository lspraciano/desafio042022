import {clearDataTables, loadDataOnTables} from "./table-controller.js";

const searchButton = document.getElementById("search-zone__button");
const datePicker = document.getElementById("search-zone__term");


const getDataAndLoad = async () => {
    let dateFromdatePikcer = datePicker.value;

    if (dateFromdatePikcer === '') {
        alert('invalid date');
        return;
    }

    dateFromdatePikcer = dateFromdatePikcer + '-02';
    const date = new Date(dateFromdatePikcer);
    await clearDataTables();
    await loadDataOnTables(date);

}

searchButton.addEventListener('click', getDataAndLoad)
import {loadDataOnTableDescribed} from "./load-data-on-table-described.js";

(() => {

    const input = document.getElementById("search__term");
    const tableTransactionLogs = document.getElementById("table-zone__table-transaction-logs");
    const tableTransactionLogsBody = document.getElementById("table-transaction-logs__body");
    const tableTransactionDescribe = document.getElementById("table-zone__table-transaction-described");


    const showOrHideTables = () => {
        const TableTransactionLogsDisplay = window.getComputedStyle(tableTransactionLogs, null).display;

        if (TableTransactionLogsDisplay === 'none') {
            tableTransactionLogs.style.display = 'table';
            tableTransactionDescribe.style.display = 'none';
            input.value = "";


        } else {
            tableTransactionLogs.style.display = 'none';
            tableTransactionDescribe.style.display = 'table';
            input.value = "";
        }
    }

    tableTransactionLogsBody.addEventListener("dblclick", async (e) => {
        showOrHideTables();
        const dateFromClick = e.target.parentElement.cells[1].innerText;
        await loadDataOnTableDescribed(dateFromClick);

    })

})()
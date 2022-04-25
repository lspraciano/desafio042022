const transactionImportSubOptions = document.getElementById("suboption_import");
const transactionAuditSubOptions = document.getElementById("suboption_audit");
const dashboardOptions = document.getElementById("menu-body__option-dashboard");
const iframeToHtml = document.getElementById("plotting-zone__frame-to-html");


async function callDashboardScreen() {
    iframeToHtml.src = '';
}


function callImportTransactionScreen() {
    iframeToHtml.src = '/transaction/import-csv';
}

function callAuditTransactionScreen() {
    iframeToHtml.src = '/transaction/log';
}

function checkIfRedirected() {
    if (iframeToHtml.contentWindow.document.title === 'Bem-Vindo'){
        location.reload();
    }
}


dashboardOptions.addEventListener('click', callDashboardScreen);
transactionImportSubOptions.addEventListener('click', callImportTransactionScreen);
transactionAuditSubOptions.addEventListener('click', callAuditTransactionScreen);
iframeToHtml.addEventListener('load', checkIfRedirected);

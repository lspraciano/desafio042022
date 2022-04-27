const transactionImportSubOptions = document.getElementById("suboption_import");
const transactionAuditSubOptions = document.getElementById("suboption_audit");
const dashboardOptions = document.getElementById("menu-body__option-dashboard");
const iframeToHtml = document.getElementById("plotting-zone__frame-to-html");
const screenName = document.getElementById("screen-name");


async function callDashboardScreen() {
    iframeToHtml.src = '';
    screenName.innerText = 'Dashboard'
}


function callImportTransactionScreen() {
    iframeToHtml.src = '/transaction/import-csv';
    screenName.innerText = 'Importar Transações'
}

function callAuditTransactionScreen() {
    iframeToHtml.src = '/transaction/log';
    screenName.innerText = 'Log de Transações'
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

import {showAndHideMenuZoneSubOptions} from "./side-bar-animation.js";

const dashboardOptions = document.getElementById("menu-body__option-dashboard");
const transactionImportSubOptions = document.getElementById("suboption_import");
const transactionAuditSubOptions = document.getElementById("suboption_audit");
const userManagerSubOptions = document.getElementById("suboption_user-manager");

const iframeToHtml = document.getElementById("plotting-zone__frame-to-html");
const screenName = document.getElementById("screen-name");


const callDashboardScreen = async () => {
    iframeToHtml.src = '';
    screenName.innerText = 'Dashboard'
    showAndHideMenuZoneSubOptions();
}


const callImportTransactionScreen = () => {
    iframeToHtml.src = '/transaction/import-csv';
    screenName.innerText = 'Importar Transações';
    showAndHideMenuZoneSubOptions();
}

const callAuditTransactionScreen = () =>  {
    iframeToHtml.src = '/transaction/log';
    screenName.innerText = 'Log de Transações';
    showAndHideMenuZoneSubOptions();
}

const callUserManagerSubOptionsScreen = () =>  {
    iframeToHtml.src = '/user/manager';
    screenName.innerText = 'Gerenciar Usuários';
    showAndHideMenuZoneSubOptions();
}


const checkIfRedirected = () =>  {
    if (iframeToHtml.contentWindow.document.body.innerHTML.indexOf("unauthorized") !== -1){
        window.location.href = window.location.origin;
    }
}


dashboardOptions.addEventListener('click', callDashboardScreen);
transactionImportSubOptions.addEventListener('click', callImportTransactionScreen);
transactionAuditSubOptions.addEventListener('click', callAuditTransactionScreen);
userManagerSubOptions.addEventListener('click', callUserManagerSubOptionsScreen);
iframeToHtml.addEventListener('load', checkIfRedirected);

const userNameInput = document.getElementById("user-name-zone__input");
const userEmailInput = document.getElementById("user-email-zone__input");
const userStatusCheckBox = document.getElementById("input-zone__value-status");

export const loadDataOnForm = (userName, userEmail, userStatus) => {
    userNameInput.value = userName;
    userEmailInput.value = userEmail;
    userStatusCheckBox.checked = userStatus === 'ATIVO';
}

export const resetDataForm = () => {
    userNameInput.value = '';
    userEmailInput.value = '';
    userStatusCheckBox.checked = true;
}
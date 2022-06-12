const formTitle = document.getElementById("form__title");
const formButton = document.getElementById("form__button");
const inputUserName = document.getElementById("input-zone__input-user-name");
const inputUserToken = document.getElementById("input-zone__input-user-token");
const inputUserPassword = document.getElementById("input-zone__input-user-password");
const inputUserPasswordConfirmation = document.getElementById("input-zone__input-user-password-confirmation");
const image = document.getElementById("figure-zone__image");


const controlStep = async () => {

    if (window.getComputedStyle(inputUserName, null).display === 'inline-block') {
        formTitle.innerText = 'Qual seu Token';
        inputUserName.style.display = 'none';
        inputUserToken.style.display = 'inline-block';
        inputUserPassword.style.display = 'none';
        inputUserPasswordConfirmation.style.display = 'none';
        image.src = './static/images/user_password_recovery/undraw_token.svg';
        return;
    }

    if (window.getComputedStyle(inputUserToken, null).display === 'inline-block') {
        formTitle.innerText = 'Escolha sua Senha';
        inputUserName.style.display = 'none';
        inputUserToken.style.display = 'none';
        inputUserPassword.style.display = 'inline-block';
        inputUserPasswordConfirmation.style.display = 'inline-block'
        image.src = './static/images/user_password_recovery/undraw_password.svg';
        return;
    }

    if (window.getComputedStyle(inputUserPasswordConfirmation, null).display === 'inline-block') {
        formTitle.innerText = 'Sua Senha foi Atualizada';
        formButton.value = 'Finalizar';
        inputUserName.style.display = 'none';
        inputUserToken.style.display = 'none';
        inputUserPassword.style.display = 'none';
        inputUserPasswordConfirmation.style.display = 'none'
        image.src = './static/images/user_password_recovery/undraw_ok.svg';
        return;
    }

    if (formTitle.innerText === 'Sua Senha foi Atualizada') {
        window.location.href = `${window.location.origin}/`;
    }

}


formButton.addEventListener('click', async () => {
    await controlStep();
})
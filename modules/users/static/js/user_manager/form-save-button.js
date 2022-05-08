import {getFormData, validateForm} from "./form-data-controller.js";
import {saveUser} from "./post-user.js";


const backButton = document.getElementById("buton-zone__btn--save");


const saveButtonEvent = async () => {

    if (await validateForm() !== false) {
        const formData = await getFormData();

        let cod = formData[0];
        let username = formData[1];
        let email = formData[2];
        let status = formData[3];

        const saveUserResult = await saveUser(cod, username, email, status);

        if ('error' in saveUserResult) {
            alert(saveUserResult['error']);
        } else {
            alert('Usuário salvo com sucesso');
            window.location.reload();
        }
    }

}

backButton.addEventListener('click', saveButtonEvent)


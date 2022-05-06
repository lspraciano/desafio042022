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
        await console.log(saveUserResult);

        alert('Usuário salvo com sucesso');

    }

}

backButton.addEventListener('click', saveButtonEvent)


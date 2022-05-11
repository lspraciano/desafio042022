import {getFormData, validateForm} from "./form-data-controller.js";
import {saveNewUser} from "./post-user.js";
import {updateUser} from "./update-user.js";


const backButton = document.getElementById("buton-zone__btn--save");


const saveButtonEvent = async () => {

    if (await validateForm() !== false) {
        const formData = await getFormData();

        let cod = parseInt(formData[0]);
        let username = formData[1];
        let email = formData[2];
        let status = formData[3];
        let result = {}

        if (status === true) {
            status = 1;
        } else {
            status = 0;
        }

        if (cod === '') {
            result = await saveNewUser(username, email);
        } else {
            result = await updateUser(cod, username, email, status);
        }

        if ('error' in result) {
            alert(result['error']);
        } else {
            alert('user saved successfully');
            window.location.reload();
        }
    }

}

backButton.addEventListener('click', saveButtonEvent)


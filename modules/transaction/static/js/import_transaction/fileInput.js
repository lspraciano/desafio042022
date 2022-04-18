import {validateInputFile} from "./validateInputFile.js";

(() => {
    const fileInput = document.getElementById('input-file');
    const title = document.getElementById('title');
    const iconOn = document.getElementById('card-zone__mid__icon-on');
    const iconOff = document.getElementById('card-zone__mid__icon-off');
    const sendButton = document.getElementById('card-zone__bottom__button');

    const handleFiles = () => {
        const selectedFiles = fileInput.files[0];

        if (validateInputFile(selectedFiles)) {
            title.innerHTML = selectedFiles.name;
            iconOn.style.display = 'flex';
            iconOff.style.display = 'none';
            sendButton.style.display = 'block';
        } else {
            alert('Arquivo Inválido !!!!')
            document.location.reload();
        }
    }


    fileInput.addEventListener("change", handleFiles);
})();
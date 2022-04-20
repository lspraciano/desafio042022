const sendButton = document.getElementById("card-zone__bottom__button");

function sendCsv() {
    alert('Arquivo enviado com sucesso!!!');
    location.reload();
}

sendButton.addEventListener('click', sendCsv);
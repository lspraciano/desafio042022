import {readCsv} from "./read-csv.js";
import {preProcessingData} from "./pre-processing-data.js";
import {getDataForDashboard} from "./save-transactions.js";

const sendButton = document.getElementById("card-zone__bottom__button");
const fileInput = document.getElementById('input-file');

const sendCsv = async () => {
    const data = await readCsv(fileInput.files[0]);
    const processedData = await preProcessingData(data);
    const result = await getDataForDashboard(processedData);
    console.log(result);

    alert('Arquivo enviado com sucesso!!!');

    // location.reload();
}

sendButton.addEventListener('click', sendCsv);
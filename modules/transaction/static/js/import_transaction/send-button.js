import {readCsv} from "./read-csv.js";
import {preProcessingData} from "./pre-processing-data.js";
import {saveTransactions} from "./save-transactions.js";

const sendButton = document.getElementById("card-zone__bottom__button");
const fileInput = document.getElementById('input-file');

const sendCsv = async () => {
    const data = await readCsv(fileInput.files[0]);
    const processedData = await preProcessingData(data);
    const result = await saveTransactions(processedData);

    if('error' in result) {
        let error = result['error']['error']['type']
        alert('As transações NÃO foram salvas. Erro: ' + error);
    } else {
        alert('Transações importadas com SUCESSO!!!');
    }

    location.reload();


}

sendButton.addEventListener('click', sendCsv);
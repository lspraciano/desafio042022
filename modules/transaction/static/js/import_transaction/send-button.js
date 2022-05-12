import {readCsv} from "./read-csv.js";
import {preProcessingData} from "./pre-processing-data.js";
import {saveTransactions} from "./save-transactions.js";

const sendButton = document.getElementById("card-zone__bottom__button");
const fileInput = document.getElementById('input-file');

const sendCsv = async () => {
    const data = await readCsv(fileInput.files[0]);
    const processedData = await preProcessingData(data);
    const result = await saveTransactions(processedData.outputValidData);

    if('error' in result) {
        alert(result['error']);
    } else {
        alert('file saved successfully');
    }

    location.reload();


}

sendButton.addEventListener('click', sendCsv);
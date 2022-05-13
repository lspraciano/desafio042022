import {readCsv} from "./read-csv.js";
import {preProcessingData} from "./pre-processing-data.js";
import {saveTransactions} from "./save-transactions.js";
import {checkCookie} from "../../../../../resources/js/cookie/cookie-manager.js";

const sendButton = document.getElementById("card-zone__bottom__button");
const fileInput = document.getElementById('input-file');

const sendCsv = async () => {
    const data = await readCsv(fileInput.files[0]);
    const processedData = await preProcessingData(data);

    if(await checkCookie() !== true) {
         window.location.href = window.location.origin;
         return;
    }

    const result = await saveTransactions(processedData.outputValidData);

    if('error' in result) {
        alert(result['error']);
    } else {
        alert('file saved successfully');
    }

    location.reload();


}

sendButton.addEventListener('click', sendCsv);
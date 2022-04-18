import {readCsv} from "./read-csv.js";

export const validateInputFile = async (file) => {
    if (file.type !== 'text/csv') {
        return false
    }
    const data = await readCsv(file);
    console.log(data)
    return true
}

import {readCsv} from "./readCsv.js";

export const validateInputFile = async (file) => {
    if (file.type !== 'text/csv') {
        return false
    }
    const data = await readCsv(file);
    return true
}

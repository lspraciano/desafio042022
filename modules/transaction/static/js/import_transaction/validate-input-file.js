export const validateInputFile = async (file) => {
    return file.type === 'text/csv';
}


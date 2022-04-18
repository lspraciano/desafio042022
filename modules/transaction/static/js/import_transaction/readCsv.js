export async function readCsv(file) {
    return new Promise((resolve, reject) => {
        Papa.parse(file, {
            header: true,
            skipEmptyLines: true,
            complete: (results) => {
                return resolve(results.data);
            },
            error: (error) => {
                return reject(error);
            },
        });
    });
}


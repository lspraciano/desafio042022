    export const saveTransactions = async (transaction) => {

        const url = `${window.location.origin}/transaction/`;
        const param = {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(transaction.outputValidData)

        }

        const response = await fetch(url, param);
        return await response.json();
    }
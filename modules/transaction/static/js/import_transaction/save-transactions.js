export const getDataForDashboard = async (transaction) => {

        const url = `${window.location.origin}/transaction/`;
        const param = {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(transaction.outputValidData)

        }

        const response = await fetch(url, param);
        const data = await response.json();

        return data;
    }
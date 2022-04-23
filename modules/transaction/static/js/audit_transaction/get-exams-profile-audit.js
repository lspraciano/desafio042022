export const getExamsProfilesAudit = async () => {

        const url = `${window.location.origin}/exams/exams-profiles-audit`;
        const param = {
            method: "GET",
            headers: {
                "Content-type": "application/json"
            }
        }

        const response = await fetch(url, param);
        const data = await response.json();

        return data;
    }
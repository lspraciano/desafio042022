export const saveUser = async (cod, username, email, status) => {

    const user = {
        "user_cod": cod,
        "username": username,
        "user_email": email,
        "user_status": status
    };

    const url = `${window.location.origin}/user/`;
    const param = {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(user)

    }

    const response = await fetch(url, param)

    return response.json()
}
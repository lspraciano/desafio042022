export const updateUser = async (cod, username, email, status) => {

    const user = {
        "user_id": cod,
        "user_name": username,
        "user_email": email,
        "user_status": status,
        "user_password": null,
        "user_token": null
    };

    const url = `${window.location.origin}/user/`;
    const param = {
        method: "UPDATE",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(user)

    }

    const response = await fetch(url, param)

    return response.json()
}
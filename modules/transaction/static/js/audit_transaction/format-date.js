export const formatOrderDate = (date) => {

    date = new Date(date);
    return (date.getDate()) + "/" +
        ((date.getMonth() + 1)) + "/" +
        date.getFullYear() + " " +
        date.getHours() + ":" +
        date.getMinutes() + ":" +
        date.getSeconds()
}


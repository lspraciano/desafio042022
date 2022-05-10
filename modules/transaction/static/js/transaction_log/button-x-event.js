(() => {

    const searchButton = document.getElementById("search__button-back");
    const input = document.getElementById("search__term");

    const callEvent = () => {
        input.value = "";

    }

    searchButton.addEventListener("click", callEvent);

})()
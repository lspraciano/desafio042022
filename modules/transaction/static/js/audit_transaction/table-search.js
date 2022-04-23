(() => {

    const btn = document.getElementById("search__button");
    const input = document.getElementById("search__term");
    const tableBody = document.getElementById("table-exams__body");

    function filterExams() {

        for (let i in tableBody.rows) {

            let cellValue = (tableBody.rows[i].cells[0]).innerHTML;
            let text = (input.value).toUpperCase();

            if (cellValue.includes(text)) {
                tableBody.rows[i].style.display = 'table-row';
            } else {
                tableBody.rows[i].style.display = 'none';
            }

        }

    }


    btn.addEventListener('click', filterExams);
    input.addEventListener("input", filterExams);

}) ()
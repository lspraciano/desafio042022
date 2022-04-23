const tableBody = document.getElementById("table-exams__body");

export const colorTableWhereChanged = (data) => {

    const examsSet = new Set();

    for (let rowAudit of data['exams_profile_audit']) {
        examsSet.add(rowAudit['exam_profile_exam']);
    }

    for (let exam of examsSet) {
        let listRowsOrderByExams = [];

        for (let r of tableBody.rows) {
            let cellValue = (r.cells[0]).innerHTML;

            if (cellValue.includes(exam)) {
                listRowsOrderByExams.push(r)
            }
        }

        for (let [i, r] of listRowsOrderByExams.entries()) {
            if (i+1 >= listRowsOrderByExams.length) {
                break;
            }

            if ((r.cells[2]).innerHTML !== (listRowsOrderByExams[i+1].cells[2]).innerHTML) {
                r.cells[2].style.fontWeight = "bold";
                r.cells[2].style.color = "red";
            }

            if ((r.cells[3]).innerHTML !== (listRowsOrderByExams[i+1].cells[3]).innerHTML) {
                r.cells[3].style.fontWeight = "bold";
                r.cells[3].style.color = "red";
            }

            if ((r.cells[4]).innerHTML !== (listRowsOrderByExams[i+1].cells[4]).innerHTML) {
                r.cells[4].style.fontWeight = "bold";
                r.cells[4].style.color = "red";
            }

        }

    }

    // for (let i in tableBody.rows) {3
    // console.log(tableBody.rows[i] == tableBody.rows[0])
    // }

}
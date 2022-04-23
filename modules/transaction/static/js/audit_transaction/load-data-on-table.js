import {getExamsProfilesAudit} from "./audit-get-exams-profile-audit.js";
import {formatOrderDate} from "./audit-format-date.js";
import {colorTableWhereChanged} from "./audit-color-change-table.js";


(() => {

    const tableBodyExams = document.getElementById("table-exams__body");

    const loadData = async () => {

        const data = await getExamsProfilesAudit();

        for (let i in data['exams_profile_audit']) {
            let row = document.createElement('tr');

            let rowExam = document.createElement('td');
            rowExam.innerHTML = data['exams_profile_audit'][i]['exam_profile_exam'];

            let rowAnalyzer = document.createElement('td');
            rowAnalyzer.innerHTML = data['exams_profile_audit'][i]['exam_profile_analyzer'];

            let rowCritMin = document.createElement('td');
            rowCritMin.innerHTML = data['exams_profile_audit'][i]['exam_profile_crit_val_min'];

            let rowCritMax = document.createElement('td');
            rowCritMax.innerHTML = data['exams_profile_audit'][i]['exam_profile_crit_val_max'];

            let rowDataStatus = document.createElement('td');
            if (data['exams_profile_audit'][i]['exam_profile_stats'] === 1) {
                rowDataStatus.innerHTML = 'ATIVO';
            } else {
                rowDataStatus.innerHTML = 'INATIVO';
            }

            let rowUser = document.createElement('td');
            rowUser.innerHTML = data['exams_profile_audit'][i]['exam_profile_user_rl']['user_name'];

            let rowDate = document.createElement('td');
            let date = new Date(data['exams_profile_audit'][i]['exam_profile_transaction_date_time']);
            rowDate.innerHTML = formatOrderDate(date);

            row.appendChild(rowExam);
            row.appendChild(rowAnalyzer);
            row.appendChild(rowCritMin);
            row.appendChild(rowCritMax);
            row.appendChild(rowDataStatus);
            row.appendChild(rowUser);
            row.appendChild(rowDate);

            tableBodyExams.appendChild(row);
        }

        colorTableWhereChanged(data)
    }

    document.addEventListener("DOMContentLoaded", async () => {
        await loadData();

    })

})()
export const plotGrapTwo = (labels, values) => {
    const canvasGraphTwo = document.getElementById('graph-two').getContext('2d');
    const data = {
        labels: labels,
        datasets: [{
            label: 'Transsações / Banco',
            data: values,
            hoverOffset: 4
        }]
    };

    const config = {
        type: 'doughnut',
        data: data,
        options: {
            maintainAspectRatio: false,
            responsive: true,
        },
    };

    const myChart = new Chart(canvasGraphTwo, config);
}
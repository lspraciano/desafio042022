export const plotGrapOne = (labels, values) => {
    const canvasGraphOne = document.getElementById('graph-one').getContext('2d');

    let gradient = canvasGraphOne.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, "rgba(82,83,163,0.7)");
    gradient.addColorStop(1, "rgba(82,83,163,0.7)");

    const data = {
        labels: labels,
        datasets: [{
            label: 'Total de Transações / Dia',
            data: values,
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    }

    const config = {
        type: 'line',
        data: data,
        options: {
            maintainAspectRatio: false,
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        },
    };

    const myChart = new Chart(canvasGraphOne, config);
}
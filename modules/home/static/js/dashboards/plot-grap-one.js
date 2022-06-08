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
            fill: true,
            backgroundColor: gradient,
        }]
    }

    const config = {
        type: 'bar',
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
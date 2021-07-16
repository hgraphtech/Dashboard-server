

// charts //

var ctx = document.getElementById('myChart')

var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      data: [],
      pointRadius: 0,
      lineTension: 0,
      backgroundColor: 'transparent',
      borderColor: '#007bff',
      borderWidth: 2,
      pointBackgroundColor: '#007bff'
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: false
        }
      }]
    },
    legend: {
      display: false
    }
  }
})



function updatechart(data) {
  var c = $('#commod_chart').val();
  myChart.data.labels = data.dates;
  myChart.data.datasets[0].data = data.prices[c].price_series;
  myChart.update();
}

function changeData() {
  fetch('/api/price')
    .then(res => res.json())
    .then(data => obj=data)
    .then(() => updatechart(obj))
}


changeData();

$('#commod_chart').on('change', changeData)

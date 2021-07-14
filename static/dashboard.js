
// table data //


let table = document.getElementById('pricetablebody');


// charts //


var ctx = document.getElementById('myChart')


var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: dates,
    datasets: [{
      data: prices[0].price_series,
      lineTension: 0,
      backgroundColor: 'transparent',
      borderColor: '#007bff',
      borderWidth: 4,
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


function changedata() {
  var c = $('#commod_chart').val();
  myChart.data.datasets[0].data = prices[c].price_series;
  myChart.update();
}


$('#commod_chart').on('change', changedata)

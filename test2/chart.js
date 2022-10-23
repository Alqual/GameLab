async function chartIt() { // Organize the `chart.js` related code line into a function
      const data = await getData(); // Get resulting data from the getData() function.
      const ctx = document.getElementById('myChart').getContext('2d');
      const myChart = new Chart(ctx, {
          type: 'line', // Switch the graph to a line chart
          data: {
              labels: data.xs, // Customize the label sources
              datasets: [{
                  label: 'Combined Land-Surface Air and Sea-Surface Water Temperature (℃)', // new name
                  data: data.ys, // Customize the data source for the Y-axis
                  fill: false, // Do not fill the line
                  backgroundColor: 'rgba(255, 99, 132, 0.2)', // Adopt single color scheme across different datasets
                  borderColor: 'rgba(255, 99, 132, 1)', // adopt single color scheme across different datasets
                  borderWidth: 1
              }]
          },
          options: {
              scales: {
                  yAxes: [{
                      ticks: {
                          // Include a ℃ sign in the ticks
                          callback: function(value, index, values) {
                              return value + '℃';
                          }
                      }
                  }]
              }
          }
      });
  }
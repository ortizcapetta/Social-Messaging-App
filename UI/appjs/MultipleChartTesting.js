
      // Load Charts and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Draw the pie chart for Ale's pizza when Charts is loaded.
      google.charts.setOnLoadCallback(drawAleChart);

      // Draw the pie chart for the Anthony's pizza when Charts is loaded.
      google.charts.setOnLoadCallback(drawAnthonyChart);
	  
	  // Draw the pie chart for the Gusti's pizza when Charts is loaded.
      google.charts.setOnLoadCallback(drawGustiChart);

      // Callback that draws the pie chart for Ale's pizza.
      function drawAleChart() {

        // Create the data table for Ale's pizza.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([
          ['Mushrooms', 1],
          ['Onions', 1],
          ['Olives', 2],
          ['Zucchini', 2],
          ['Pepperoni', 1]
        ]);

        // Set options for Ale's pie chart.
        var options = {title:'How Much Pizza Ale Ate Last Night',
                       width:400,
                       height:300};

        // Instantiate and draw the chart for Ale's pizza.
        var chart = new google.visualization.PieChart(document.getElementById('Ale_chart_div'));
        chart.draw(data, options);
      }

      // Callback that draws the pie chart for Anthony's pizza.
      function drawAnthonyChart() {

        // Create the data table for Anthony's pizza.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([
          ['Mushrooms', 2],
          ['Onions', 2],
          ['Olives', 2],
          ['Zucchini', 0],
          ['Pepperoni', 3]
        ]);

        // Set options for Anthony's pie chart.
        var options = {title:'How Much Pizza Anthony Ate Last Night',
                       width:400,
                       height:300};

        // Instantiate and draw the chart for Anthony's pizza.
        var chart = new google.visualization.PieChart(document.getElementById('Anthony_chart_div'));
        chart.draw(data, options);
      }
	  
	  // Callback that draws the pie chart for Gusti's pizza.
      function drawGustiChart() {

        // Create the data table for Gusti's pizza.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([
          ['Mushrooms', 1],
          ['Onions', 1],
          ['Olives', 2],
          ['Zucchini', 2],
          ['Pepperoni', 1]
        ]);

        // Set options for Gusti's pie chart.
        var options = {title:'How Much Pizza Gusti Ate Last Night',
                       width:400,
                       height:300};

        // Instantiate and draw the chart for Gusti's pizza.
        var chart = new google.visualization.PieChart(document.getElementById('Gusti_chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <!--Table and divs that hold the pie charts-->
    <table class="columns">
      <tr>
        <td><div id="Ale_chart_div" style="border: 1px solid #ccc"></div></td>
        <td><div id="Anthony_chart_div" style="border: 1px solid #ccc"></div></td>
		<td><div id="Gusti_chart_div" style="border: 1px solid #ccc"></div></td>
      </tr>
    </table>
  </body>
</html>

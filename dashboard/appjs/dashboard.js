// Load the Visualization API and the piechart package.
google.charts.load('current', {'packages': ['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawHashtagsChart);

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawMessagesChart);

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawRepliesChart);

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawLikesChart);

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawDislikesChart);

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawUsersChart);

/**
function reformatData(jsonData){
    var temp= jsonData.PartCounts;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        dataElement.push(row.id + '-' + row.name);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}
*/

// Draw Trending topics via #hashtags (top 10)
function drawHashtagsChart() {
    
    var jsonData = $.ajax({
        url: "http://localhost:5000/charts/hashtags",
        dataType: "json",
        async: false
    }).responseText;

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Hashtag');
    data.addColumn('number', 'Count');
    data.addRows(JSON.parse(jsonData));

    var options = {
        title: 'Top 10 Hashtags',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Uses',
            minValue: 0
        },
        vAxis: {
            title: 'Hashtag'
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('hashtags_div'));

    chart.draw(data, options);

}



// Draw number of messages per day
function drawMessagesChart() {
    
    var jsonData = $.ajax({
        url: "http://localhost:5000/charts/messages",
        dataType: "json",
        async: false
    }).responseText;

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Count');
    data.addColumn('datetime', 'Date');
    data.addRows(JSON.parse(jsonData));

    var options = {
        title: 'Messages per date',
        curveType: 'function',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Date',
            minValue: 0
        },
        vAxis: {
            title: 'Number of Messages'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('messages_div'));

    chart.draw(data, options);

}


// Draw number of replies per day
function drawRepliesChart() {
    
    var jsonData = $.ajax({
        url: "http://localhost:5000/charts/replies",
        dataType: "json",
        async: false
    }).responseText;

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Count');
    data.addColumn('datetime', 'Date');
    data.addRows(JSON.parse(jsonData));

    var options = {
        title: 'Replies per date',
        curveType: 'function',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Date',
            minValue: 0
        },
        vAxis: {
            title: 'Number of Replies'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('replies_div'));

    chart.draw(data, options);

}


// Draw number of likes per day
function drawLikesChart() {
    
    var jsonData = $.ajax({
        url: "http://localhost:5000/charts/likes",
        dataType: "json",
        async: false
    }).responseText;

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Count');
    data.addColumn('datetime', 'Date');
    data.addRows(JSON.parse(jsonData));

    var options = {
        title: 'Likes per date',
        curveType: 'function',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Date',
            minValue: 0
        },
        vAxis: {
            title: 'Number of Likes'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('likes_div'));

    chart.draw(data, options);

}


// Draw number of dislikes per day
function drawDislikesChart() {
    
    var jsonData = $.ajax({
        url: "http://localhost:5000/charts/dislikes",
        dataType: "json",
        async: false
    }).responseText;

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Count');
    data.addColumn('datetime', 'Date');
    data.addRows(JSON.parse(jsonData));

    var options = {
        title: 'Dislikes per date',
        curveType: 'function',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Date',
            minValue: 0
        },
        vAxis: {
            title: 'Number of Dislikes'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('dislikes_div'));

    chart.draw(data, options);

}


// Draw number of active users posting messages or replies per day
function drawUsersChart() {
    
    var jsonData = $.ajax({
        url: "http://localhost:5000/charts/users",
        dataType: "json",
        async: false
    }).responseText;

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Count');
    data.addColumn('datetime', 'Date');
    data.addRows(JSON.parse(jsonData));

    var options = {
        title: 'Active users per date',
        curveType: 'function',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Date',
            minValue: 0
        },
        vAxis: {
            title: 'Active Users'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('users_div'));

    chart.draw(data, options);

}



google.charts.load('current', {packages: ['corechart', 'bar', 'line']});
google.charts.setOnLoadCallback(drawHashtagsChart);
google.charts.setOnLoadCallback(drawMessagesChart);
google.charts.setOnLoadCallback(drawRepliesChart);
google.charts.setOnLoadCallback(drawLikesChart);
google.charts.setOnLoadCallback(drawDislikesChart);
google.charts.setOnLoadCallback(drawUsersChart);

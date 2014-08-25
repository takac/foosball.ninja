(function() {
    console.log("hello world");
    get_epochs = function(d) {
        return d.map(function(a){
            return Number.parseInt(a.gamedate);
        })
    }

    var filter_data = function(filter, data) {
        return get_epochs(data.filter(filter))
            .sort(function(a, b) {
                    return a - b;
                })
            .reduce(function(acc, n) {
                d = new Date(0);
                d.setUTCSeconds(n)
                    acc.push({
                        'epoch': n,
                        'n': acc.length+1,
                        'date': d
                    });
                    return acc;
                }, []);
    }

    var margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = 1060 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    var xscale = d3.time.scale()
        .range([0, width]);
    var yscale = d3.scale.linear()
        .range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(xscale)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(yscale)
        .orient("left");

    var line = d3.svg.line()
        .x(function(d) { return xscale(d.date); })
        .y(function(d) { return yscale(d.n); });

    var svg = d3.select("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    d3.json("/player/" + window.player_id + "/results.json", function(error, data) {
        data = data.results;

        var all = filter_data(function(a) { return true; }, data);
        var winning = filter_data(function(a) { return a.won }, data);
        var losing = filter_data(function(a) { return !a.won }, data);

        yscale.domain(d3.extent(all, function(d) { return d.n; }));
        xscale.domain(d3.extent(all, function(d) { return d.date; }));

        svg.append("g")
              .attr("class", "x axis")
              .attr("transform", "translate(0," + height + ")")
              .call(xAxis);

          svg.append("g")
              .attr("class", "y axis")
              .call(yAxis)
            .append("text")
              .attr("transform", "rotate(-90)")
              .attr("y", 6)
              .attr("dy", ".71em")
              .style("text-anchor", "end")
              .text("Games");

          svg.append("path")
              .datum(losing)
              .attr("class", "line")
              .attr("d", line)
              .attr("stroke", "red");

          svg.append("path")
              .datum(winning)
              .attr("class", "line")
              .attr("d", line)
              .attr("stroke", "steelblue");
    });
})();

$(function() {
  console.log('jquery is working!');
  createGraph();
});

function createGraph() {

    // REQUEST THE DATA
    d3.json("/data", function(error, elasticdata) {
        console.log(elasticdata.aggregations.allSourceAgg.buckets)
        
        var raw_data = elasticdata.aggregations.allSourceAgg.buckets;
        var data = []

        for (var i in raw_data) {
            data.push(raw_data[i].doc_count);
        }

        var width = 960,
            height = 500;

        var outerRadius = height / 2 - 20,
            innerRadius = outerRadius / 3,
            cornerRadius = 10;

        var pie = d3.layout.pie()
            .padAngle(.02);

        var arc = d3.svg.arc()
            .padRadius(outerRadius)
            .innerRadius(innerRadius);

        var svg = d3.select("body").append("svg")
            .attr("width", width)
            .attr("height", height)
          .append("g")
            .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

        svg.selectAll("path")
            .data(pie(data))
            .enter().append("path")
            .each(function(d) { d.outerRadius = outerRadius - 20; })
            .attr("d", arc)
            .on("mouseover", arcTween(outerRadius, 0))
            .on("mouseout", arcTween(outerRadius - 20, 150));

        function arcTween(outerRadius, delay) {
          return function() {
            d3.select(this).transition().delay(delay).attrTween("d", function(d) {
              var i = d3.interpolate(d.outerRadius, outerRadius);
              return function(t) { d.outerRadius = i(t); return arc(d); };
            });
          };
        }
    });
}

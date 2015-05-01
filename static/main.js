$(function() {
  console.log('jquery is working!');
  createGraph();
});

function createGraph() {

    var svg = d3.select("#chart").append("svg")
      .attr("width", 30)
      .attr("height", 30)
      .attr("class", "bubble");

    // REQUEST THE DATA
    d3.json("/data", function(error, elasticdata) {
        console.log(elasticdata)
        var node = svg.selectAll('.node')
        // .data(bubble.nodes(quotes)
        // .filter(function(d) { return !d.children; }))
        // .enter().append('g')
        // .attr('class', 'node')
        // .attr('transform', function(d) { return 'translate(' + d.x + ',' + d.y + ')'});

    });
}

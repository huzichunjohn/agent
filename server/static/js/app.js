var width = 400,
    height = 400;
var svg = d3.select("body")
    .append("svg")
    .attr("width", width)
    .attr("height", height);
svg.append("circle")
    .attr("cx", 100)
    .attr("cy", 100)
    .attr("r", 20);
svg.append("rect")
    .attr("x", 50)
    .attr("y", 50)
    .attr("width", 30)
    .attr("height", 50)
    .attr("fill", "red");

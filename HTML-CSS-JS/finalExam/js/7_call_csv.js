d3.csv("https://psw7205.github.io/D3jsPractices/grade.csv", function (error, data) {
    var dataset = [];

    for (var i = 0; i < data.length; i++) {
        dataset.push(data[i].datascience);
    }

    d3.select("#myGraph")
        .selectAll("rect")
        .data(dataset)
        .enter()
        .append("rect")
        .attr("x", 0)
        .attr("y", function (d, i) {
            return i * 25;
        })
        .attr("height", "20px")
        .attr("width", function (d, i) {
            return d + "px";
        })
        .style("fill", "orange")
});
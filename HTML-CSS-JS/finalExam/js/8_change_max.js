var dataset = [300, 130, 5, 60, 240];

function findmax(arr) {
    var max = 0;
    var idx = 0;
    for (var i = 0; i < arr.length; i++) {
        if (max < arr[i]) {
            max = arr[i];
            idx = i;
        }
    }

    return idx;
}

d3.select("#myGraph")
    .selectAll("rect")
    .data(dataset)
    .enter()
    .append("rect")
    .style("fill", "red")
    .attr("class", "bar")
    .attr("width", function (d, u) {
        return d;
    })
    .attr("height", 20)
    .attr("x", 0)
    .attr("y", function (d, i) {
        return i * 25;
    })
    .style("fill", function (d, i) {
        var max_bar = document.getElementsByTagName("rect");
        d3.select(max_bar[findmax(dataset)])
            .style("fill", "blue")
    })

function updateButton() {
    for (var i = 0; i < dataset.length; i++) {
        dataset[i] = Math.floor(Math.random() * 320);
    }
    console.log(dataset);
}
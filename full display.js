// For this to work, readingx needs to be an array of data readings
// in arduino analog 0-1023 format.  Tested with strings, but integers
// should work just as well.
data.splice(0, data.length);
temperatures = readingx.map(item => mv_to_f(+item));
temperatures.forEach(item => data.push(item));

// Might need these
const graphx = window.chartThings.graph;
const linex = window.chartThings.line;

window.chartThings.x.domain([0, data.length/60]).range([margin.left, width - margin.right]);
window.chartThings.y.domain([d3.min(data, function(d) { return d; }), d3.max(data, function(d) { return d; })]);

// update axis labels
graphx.selectAll("g.y.axis").call(window.chartThings.yAxis);
graphx.selectAll("g.x.axis").call(window.chartThings.xAxis);

// re-draw data
graphx.selectAll("path").attr("d", line(data));

// Highest temperature reached
temperatures.reduce((acc, itm) => acc > itm ? acc : itm, 0);
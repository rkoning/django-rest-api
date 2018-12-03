$(document).ready(function() {
  // fetchCampaigns(1)
})

//
// performs a get request to fetch the campaigns related to an account
//
function fetchCampaigns(id) {
  let path = `/api/v1/campaigns/${id}/advertisements`
  $.ajax({
    url: path,
    type: 'GET',
    data: {filter: 'date, cost', limit: 100, order_by: 'clicks'},
    success: function(data) {
      updateBarChart(data)
    }
  })
}

function fetchAdsWithMethod(id, x, y, method, order) {
  let path = `/api/v1/campaigns/${id}/advertisements`
  $.ajax({
    url: path,
    type: 'GET',
    data: {filter: `${x},${y}`, order_by: x, order: order, method: method},
    success: function(data) {
      data = data.map(function (d) { return {x: d[x], y: d[`${y}__${method}`]}})
      updateBarChart(data, x, y)
    }
  })
}

function getGraph() {
  id = $("#campaign_id").val()
  x_field = $('#x_axis_field').val()
  y_field = $('#y_axis_field').val()
  method = $('#summary_method').val()
  order = $('#order').val()
  fetchAdsWithMethod(id, x_field, y_field, method, order)
}

function updateBarChart(data, x ,y) {
  // data = data.map(function (d) { return {category: d['fields']['region_criteria_id'], x: d['fields']['date'], y: d['fields']['cost']}})

  var margin = {top: 20, right: 20, bottom: 70, left: 40},
      width = 950 - margin.left - margin.right,
      height = 300 - margin.top - margin.bottom

  var x = d3.scaleBand()
      .range([0, width])
      .domain(data.map(function(d) { return d.x; }));

  var y = d3.scaleLinear()
      .range([height, 0])
      .domain([0, d3.max(data, function(d) { return d.y; })]);

  var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

  svg.append("g")
     .attr("transform", "translate(0," + height + ")")
     .call(d3.axisBottom(x).ticks(20, 5))
  svg.append("text")
    .attr("transform",
          "translate(" + (width/2) + " ," +
                         (height + margin.top + 20) + ")")
    .style("text-anchor", "middle")
    .text(x);

  svg.append("g")
      .call(d3.axisLeft(y)
      .ticks(10))
  svg.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left)
      .attr("x",0 - (height / 2))
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .text(x);

  svg.selectAll("bar")
      .data(data)
    .enter().append("rect")
      .style("fill", "steelblue")
      .attr("x", function(d) { return x(d.x); })
      .attr("width", x.bandwidth())
      .attr("y", function(d) { return y(d.y); })
      .attr("height", function(d) { return height - y(d.y); });


}

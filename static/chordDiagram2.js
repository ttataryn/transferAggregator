var margin = {left:90, top:90, right:90, bottom:90},
	width = Math.min(window.innerWidth, 700) - margin.left - margin.right,
    height = Math.min(window.innerWidth, 700) - margin.top - margin.bottom,
    innerRadius = Math.min(width, height) * .39,
    outerRadius = innerRadius * 1.1;

	
var Names = ["Bundesliga","Premier League","Ligue 1","La Liga","Serie A","Other","Eredivisie","EPL"],
	colors = ["#301E1E", "#083E77", "#342350", "#567235", "#8B161C", "#C0C0C0", "#DF7C00", "#6A5ACD"],
	opacityDefault = 0.8;

var matrix = [
[0,0,0,0,0,0,0,18],
[0,0,0,0,0,0,0,90],
[0,0,0,0,0,0,0,17],
[0,0,0,0,0,0,0,12],
[0,0,0,0,0,0,0,15],
[0,0,0,0,0,0,0,48],
[0,0,0,0,0,0,0,6],
[18,90,17,12,15,48,6,0]
];
// [0,0,0,0,0,0,35,5,0,10,0,0], //Math
// [0,0,0,0,0,0,10,38,0,2,0,0], //CS
// [0,0,0,0,0,0,30,10,0,20,5,0], //ECON
// [0,0,0,0,0,0,0,0,10,0,2,0], //History
// [0,0,0,0,0,0,10,5,0,5,20,0], //Comm
// [0,0,0,0,0,0,0,0,0,0,0,50], //Empty DUMMY
// [35,10,30,0,10,0,0,0,0,0,0,0], //Finance
// [5,38,10,0,5,0,0,0,0,0,0,0], //Tech
// [0,0,0,10,0,0,0,0,0,0,0,0], //Law
// [10,2,20,0,5,0,0,0,0,0,0,0], //Banking
// [0,0,5,2,20,0,0,0,0,0,0,0], //HR
// [0,0,0,0,0,50,0,0,0,0,0,0], //Empty Dummy
// ];

////////////////////////////////////////////////////////////
/////////// Create scale and layout functions //////////////
////////////////////////////////////////////////////////////

var colors = d3.scale.ordinal()
    .domain(d3.range(Names.length))
	.range(colors);

var chord = d3.layout.chord()
    .padding(.15)
    .sortChords(d3.descending)
	.matrix(matrix);
		
var arc = d3.svg.arc()
    .innerRadius(innerRadius*1.01)
    .outerRadius(outerRadius);

var path = d3.svg.chord()
	.radius(innerRadius);
	
////////////////////////////////////////////////////////////
////////////////////// Create SVG //////////////////////////
////////////////////////////////////////////////////////////
	
var svg = d3.select("#chart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
	.append("g")
    .attr("transform", "translate(" + (width/2 + margin.left) + "," + (height/2 + margin.top) + ")");



		
////////////////////////////////////////////////////////////
////////////////// Draw outer Arcs /////////////////////////
////////////////////////////////////////////////////////////

var outerArcs = svg.selectAll("g.group")
	.data(chord.groups)
	.enter().append("g")
	.attr("class", "group")
	.on("mouseover",fade(.1))
	.on("mouseout", fade(opacityDefault));
var text = outerArcs.selectAll("g").selectAll("text")
	.on("click", fade(.1))
	.on("mouseout", fade(opacityDefault));
var innerArc = svg.selectAll("path.chord")
	.on("mouseover", fade(.1))
	.on("mouseout", fade(opacityDefault));

outerArcs.append("path")
	.style("fill", function(d) { return colors(d.index); })
	.attr("d", arc);
	
////////////////////////////////////////////////////////////
////////////////////// Append Names ////////////////////////
////////////////////////////////////////////////////////////

//Append the label names on the outside
outerArcs.append("text")
  .each(function(d) { d.angle = (d.startAngle + d.endAngle) / 2; })
  .attr("dy", ".35em")
  .attr("class", "titles")
  .attr("text-anchor", function(d) { return d.angle > Math.PI ? "end" : null; })
  .attr("transform", function(d) {
		return "rotate(" + (d.angle * 180 / Math.PI - 90) + ")"
		+ "translate(" + (outerRadius + 10) + ")"
		+ (d.angle > Math.PI ? "rotate(180)" : "");
  })
  .text(function(d,i) { return Names[i]; });
	
////////////////////////////////////////////////////////////
////////////////// Draw inner chords ///////////////////////
////////////////////////////////////////////////////////////
  
svg.selectAll("path.chord")
	.data(chord.chords)
	.enter().append("path")
	.attr("class", "chord")
	.style("fill", function(d) { return colors(d.source.index); })
	.style("opacity", opacityDefault)
	.attr("d", path);

////////////////////////////////////////////////////////////
////////////////// Extra Functions /////////////////////////
////////////////////////////////////////////////////////////

//Returns an event handler for fading a given chord group.
function fade(opacity) {
  return function(d,i) {
    svg.selectAll("path.chord")
        .filter(function(d) { return d.source.index != i && d.target.index != i; })
		.transition()
        .style("opacity", opacity);
  };
}
// @TODO: YOUR CODE HERE!
// width and height for the svg
var width = parseInt(d3.select("#scatter").style("width"));
var height = width - width / 3.9;

//set up chart canvas
//margins
var margin = 20;
// labels padding
var labelArea = 110;

// padding for bottom and left axes
var tPadBot = 40;
var tPadLeft = 40;

//create canvas to place graph
var svg = d3
	.select("#scatter")
	.append("svg")
	.attr("width", width)
	.attr("height", height)
	.attr("class", "chart");

//setting radius for each graph dot
var circRadius;
function crGet() {
	if (width <= 530) {
		circRadius = 5;
	}
}
crGet();

//labels for each axis

//Bottom Axis
//============
svg.append("g").attr("class", "xText");
var xText = d3.select(".xText");

//transforming xText to place at bottom of chart
function xTextRefresh() {
	xText.attr(
		"transform",
		"translate(" + ((width - labelArea)/2 + labelArea) + ", " + (height - margin - tPadBot) + ")"
	);
}
xTextRefresh();

//use xText to append SVG files 
//Poverty SVG file
xText
	.append("text")
	.attr("y", -26)
	.attr("data-name", "poverty")
	.attr("data-axis", "x")
	.attr("class", "aText active x")
	.text ("In Poverty (%)");

//Age SVG file
xText
	.append("text")
	.attr("y", 0)
	.attr("data-name", "age")
	.attr("data-axis", "x")
	.attr("class", "aText inactive x")
	.text ("Age (Median)");

//Income SVG file
xText
	.append("text")
	.attr("y", 26)
	.attr("data-name", "income")
	.attr("data-axis", "x")
	.attr("class", "aText inactive x")
	.text ("Household Income (Median)");

//Left Axis
//specify y labels/text
var leftTextX = margin + tPadLeft;
var leftTextY = (height + labelArea)/2 - labelArea;

//adding a second label group
svg.append("g").attr("class","yText");
var yText = d3.select(".yText");

//tranform function
function yTextRefresh() {
	yText.attr(
	  "transform",
	  "translate(" + leftTextX + ", " + leftTextY + ")rotate(-90)"
	);
  }
yTextRefresh();

//y axis labels/text
//Obesity SVG file
yText
  .append("text")
  .attr("y", -26)
  .attr("data-name", "obesity")
  .attr("data-axis", "y")
  .attr("class", "aText active y")
  .text("Obese (%)");

//Smoking SVG file
yText
  .append("text")
  .attr("x", 0)
  .attr("data-name", "smokes")
  .attr("data-axis", "y")
  .attr("class", "aText inactive y")
  .text("Smokes (%)");

//Healthcare SVG file
yText
  .append("text")
  .attr("y", 26)
  .attr("data-name", "healthcare")
  .attr("data-axis", "y")
  .attr("class", "aText inactive y")
  .text("Lacks Healthcare (%)");

//Import CSV file
//=================
// This data file includes state-by-state demographic data from the US Census
// and measurements from health risks obtained
// by the Behavioral Risk Factor Surveillance System.

//Import CSV using d3.csv import method
d3.csv("assets/data/data.csv").then(function(data) {
	// Visualize the data
	visualize(data);
  });

//Create the visualization function. call up function on data from CSV
function visualize(theData) {
	//curX and curY set up to determine which data gets highlighted in each axis
	//designate default x and y here, same headings as .csv file
var curX = "poverty";
var curY = "obesity";

//save empty variables for min and max x and y values
var xMin;
var xMax;
var yMin;
var yMax;

//set up tooltip rules
var toolTip = d3
    .tip()
    .attr("class", "d3-tip")
    .offset([40, -60])
    .html(function(d) {
	  console.log(d)
	// x key
	var theX;
	// state name 
	var theState = "<div>" + d.state + "</div>";
	// grab the y value's key and value.
	var theY = "<div>" + curY + ": " + d[curY] + "%</div>";
	// If the x key is poverty
	if (curX === "poverty") {
	  // Grab the x key and a version of the value formatted to show percentage
	  theX = "<div>" + curX + ": " + d[curX] + "%</div>";
	}
	else {
        // Otherwise
        // Grab the x key and a version of the value formatted to include commas after every third digit.
        theX = "<div>" +
          curX +
          ": " +
          parseFloat(d[curX]).toLocaleString("en") +
          "</div>";
	  }
	  //Display the data captured
	  return theState + theX + theY;
});
//call the toolTip function
svg.call(toolTip);

//functions set up to remove repetition 
//change min and max for x
function xMinMax() {
    // min function to grab smallest data point from the selected column.
    xMin = d3.min(theData, function(d) {
      return parseFloat(d[curX]) * 0.90;
	});
	//max function to grab the largest data point from the selected column.
    xMax = d3.max(theData, function(d) {
		return parseFloat(d[curX]) * 1.10;
	  });
	}
//change min and max for y
function yMinMax() {
    // min function to grab the smallest data point from the selected column.
    yMin = d3.min(theData, function(d) {
      return parseFloat(d[curY]) * 0.90;
    });

    //max function to grab the largest data point from the selected column.
    yMax = d3.max(theData, function(d) {
      return parseFloat(d[curY]) * 1.10;
    });
  }

//change classes and appearance of label text when clicked
function labelChange(axis, clickedText) {
    // Switch the currently active to inactive.
    d3
      .selectAll(".aText")
      .filter("." + axis)
      .filter(".active")
      .classed("active", false)
      .classed("inactive", true);

    // Switch the text just clicked to active.
    clickedText.classed("inactive", false).classed("active", true);
  }

//Instantiate the scatter plot
//set up initial data placement to scatter plot
xMinMax();
yMinMax();

//create scales
var xScale = d3
    .scaleLinear()
    .domain([xMin, xMax])
    .range([margin + labelArea, width - margin]);
  var yScale = d3
    .scaleLinear()
    .domain([yMin, yMax])
    // Height is inverses due to how d3 calc's y-axis placement
	.range([height - margin - labelArea, margin]);
	
//create axes
var xAxis = d3.axisBottom(xScale);
var yAxis = d3.axisLeft(yScale);

//Determine x and y ticks
function tickCount() {
    if (width <= 500) {
      xAxis.ticks(5);
      yAxis.ticks(5);
    }
    else {
      xAxis.ticks(10);
      yAxis.ticks(10);
    }
  }
  tickCount();

//append axes
svg
    .append("g")
    .call(xAxis)
    .attr("class", "xAxis")
    .attr("transform", "translate(0," + (height - margin - labelArea) + ")");
svg
    .append("g")
    .call(yAxis)
    .attr("class", "yAxis")
    .attr("transform", "translate(" + (margin + labelArea) + ", 0)");

//declare circles variable
var theCircles = svg.selectAll("g theCircles").data(theData).enter();

//append circles for each state
theCircles
    .append("circle")
    // Append attributes
    .attr("cx", function(d) {
      return xScale(d[curX]);
    })
    .attr("cy", function(d) {
      return yScale(d[curY]);
    })
    .attr("r", circRadius)
    .attr("class", function(d) {
      return "stateCircle " + d.abbr;
    })
    // Hover rules
    .on("mouseover", function(d) {
      // Show the tooltip
      toolTip.show(d, this);
      // Highlight the state circle's border
      d3.select(this).style("stroke", "#323232");
    })
    .on("mouseout", function(d) {
      // Remove the tooltip
      toolTip.hide(d);
      // Remove highlight
      d3.select(this).style("stroke", "#e3e3e3");
	});
	
//add labels to state circles
theCircles
    .append("text")
    // abbreviate text.
    .text(function(d) {
      return d.abbr;
    })
    // place text.
    .attr("dx", function(d) {
      return xScale(d[curX]);
    })
    .attr("dy", function(d) {
      // When the size of the text is the radius,
      // adding a third of the radius to the height      
      return yScale(d[curY]) + circRadius / 2.5;
    })
    .attr("font-size", circRadius)
    .attr("class", "stateText")
    // Hover Rules
    .on("mouseover", function(d) {
      // Show the tooltip
      toolTip.show(d);
      // Highlighting the state circle's border
      d3.select("." + d.abbr).style("stroke", "#323232");
    })
    .on("mouseout", function(d) {
      // Remove tooltip
      toolTip.hide(d);
      // Remove highlight
      d3.select("." + d.abbr).style("stroke", "#e3e3e3");
    });

//making the graphic dynamic. user can click on label and it will display data
d3.selectAll(".aText").on("click", function() {
	var self = d3.select(this);	
	
//don't show text on inactive circles
if (self.classed("inactive")) {
	// Grab the name and axis saved in label.
	var axis = self.attr("data-axis");
	var name = self.attr("data-name");

	//when x is saved, execute
	if (axis === "x") {
        // Make curX the same as the data name.
		curX = name;
		
		//change min and max of x axis
		xMinMax();

		//update x domain
		xScale.domain([xMin, xMax]);

		//transition when updating x axis
		svg.select(".xAxis").transition().duration(300).call(xAxis);

		//update location of state circles when axis changes
		d3.selectAll("circle").each(function() {
			// Each state circle gets a transition for new attribute.
			d3
			  .select(this)
			  .transition()
			  .attr("cx", function(d) {
				return xScale(d[curX]);
			  })
			  .duration(300);
		  });

		//change location of state text when axis changes
		d3.selectAll(".stateText").each(function() {
		   d3
		   .select(this)
		   .transition()
		   .attr("dx", function(d) {
			 return xScale(d[curX]);
		   })
		   .duration(300);
	   });
 
	   //change classes of last active label and clicked label
	   labelChange (axis, self);
	}
	else {
		curY=name;

		//change min and max of y axis
		yMinMax();

		//update y domain
		yScale.domain([yMin, yMax]);

		//update y axis
		svg.select(".yAxis").transition().duration(300).call(yAxis);

		//update location of state circles when axis changes
		d3.selectAll("circle").each(function(){
			d3
				.select(this)
				.transition()
				.attr("cy", function(d) {
					return yScale(d[curY]);
				})
				.duration(300);	
		});

		//change location of state texts
		d3.selectAll(".stateText").each(function() {
			// transitions
			d3
			  .select(this)
			  .transition()
			  .attr("dy", function(d) {
				return yScale(d[curY]) + circRadius / 3;
			  })
			  .duration(300);
		  });

		  //change classes of last active label and clicked label
		  labelChange(axis, self);
		}	
	}
});

//mobile responsive design
d3.select(window).on("resize", resize);

  function resize() {
    // Redefine the width, height and leftTextY 
    width = parseInt(d3.select("#scatter").style("width"));
    height = width - width / 3.9;
    leftTextY = (height + labelArea) / 2 - labelArea;

    // Apply the width and height to the svg canvas.
    svg.attr("width", width).attr("height", height);

    // Change the xScale and yScale ranges
    xScale.range([margin + labelArea, width - margin]);
    yScale.range([height - margin - labelArea, margin]);

    // With the scales changes, update the axes 
    svg
      .select(".xAxis")
      .call(xAxis)
      .attr("transform", "translate(0," + (height - margin - labelArea) + ")");

    svg.select(".yAxis").call(yAxis);

    // Update the ticks on each axis.
	tickCount();
	
	//update labels
	xTextRefresh();
	yTextRefresh();

	//update radius of each dot
	crGet();

	//update location and radius of state circles
	d3
      .selectAll("circle")
      .attr("cy", function(d) {
        return yScale(d[curY]);
      })
      .attr("cx", function(d) {
        return xScale(d[curX]);
      })
      .attr("r", function() {
        return circRadius;
      });

    // We need change the location and size of the state texts, too.
    d3
      .selectAll(".stateText")
      .attr("dy", function(d) {
        return yScale(d[curY]) + circRadius / 3;
      })
      .attr("dx", function(d) {
        return xScale(d[curX]);
      })
      .attr("r", circRadius / 3);
  }
}

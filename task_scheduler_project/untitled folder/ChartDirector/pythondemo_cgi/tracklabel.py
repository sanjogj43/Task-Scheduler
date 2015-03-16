#!/usr/bin/python
from pychartdir import *
import cgi

# Get HTTP query parameters
query = cgi.FieldStorage()


#
# In this demo, the generated web page needs to load the "cdjcv.js" Javascript file and several GIF
# files. For ease of installation, we put these files in the same directory as this script. However,
# if this script is installed in a CGI only directory (such as cgi-bin), the web server would not
# allow the browser to access these non-CGI files.
#
# To get around this potential issue, a special load resource script is used to load these files.
# Instead of using:
#
#    <SCRIPT SRC="cdjcv.js">
#
# we now use:
#
#    <SCRIPT SRC="loadresource.py?file=cdjcv.js">
#
# Similar methods are used to load the GIF files.
#
# If this script is not in a CGI only directory, you may replace the following loadResource string
# with an empty string "" to improve performance.
#
loadResource = "loadresource.py?file="

# Data for the chart as 3 random data series
r = RanSeries(127)
data0 = r.getSeries(100, 100, -15, 15)
data1 = r.getSeries(100, 150, -15, 15)
data2 = r.getSeries(100, 200, -15, 15)
timeStamps = r.getDateSeries(100, chartTime(2011, 1, 1), 86400)

# Create a XYChart object of size 640 x 400 pixels
c = XYChart(640, 400)

# Add a title to the chart using 18 pts Times New Roman Bold Italic font
c.addTitle("    Product Line Global Revenue", "timesbi.ttf", 18)

# Set the plotarea at (50, 55) with width 70 pixels less than chart width, and height 90 pixels less
# than chart height. Use a vertical gradient from light blue (f0f6ff) to sky blue (a0c0ff) as
# background. Set border to transparent and grid lines to white (ffffff).
c.setPlotArea(50, 55, c.getWidth() - 70, c.getHeight() - 90, c.linearGradientColor(0, 55, 0,
    c.getHeight() - 35, 0xf0f6ff, 0xa0c0ff), -1, Transparent, 0xffffff, 0xffffff)

# Add a legend box at (50, 25) using horizontal layout. Use 10pts Arial Bold as font. Set the
# background and border color to Transparent.
c.addLegend(50, 25, 0, "arialbd.ttf", 10).setBackground(Transparent)

# Set axis label style to 8pts Arial Bold
c.xAxis().setLabelStyle("arialbd.ttf", 8)
c.yAxis().setLabelStyle("arialbd.ttf", 8)

# Set the axis stem to transparent
c.xAxis().setColors(Transparent)
c.yAxis().setColors(Transparent)

# Configure x-axis label format
c.xAxis().setMultiFormat(StartOfYearFilter(), "{value|mm/yyyy} ", StartOfMonthFilter(), "{value|mm}"
    )

# Add axis title using 10pts Arial Bold Italic font
c.yAxis().setTitle("USD millions", "arialbi.ttf", 10)

# Add a line layer to the chart using a line width of 2 pixels.
layer = c.addLineLayer2()
layer.setLineWidth(2)

# Add 3 data series to the line layer
layer.setXData(timeStamps)
layer.addDataSet(data0, 0xff3333, "Alpha")
layer.addDataSet(data1, 0x008800, "Beta")
layer.addDataSet(data2, 0x3333cc, "Gamma")

# Create the WebChartViewer object
viewer = WebChartViewer(query, "chart1")

# Output the chart
chartQuery = c.makeTmpFile("/tmp/tmpcharts")

# Set the chart URL to the viewer
viewer.setImageUrl("getchart.py?img=/tmp/tmpcharts/" + chartQuery)

# Output Javascript chart model to the browser to support tracking cursor
viewer.setChartModel(c.getJsChartModel())

print("Content-type: text/html\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <title>Track Line with Data Labels</title>
    <script type="text/javascript" src="%(loadResource)scdjcv.js"></script>
</head>
<body style="margin:5px 0px 0px 5px">
<script type="text/javascript">

//
// Use the window load event to set up the MouseMovePlotArea event handler
//
JsChartViewer.addEventListener(window, 'load', function() {
    var viewer = JsChartViewer.get('%(id)s');

    // Draw track cursor when mouse is moving over plotarea. Hide it when mouse leaves plot area.
    viewer.attachHandler("MouseMovePlotArea", function(e) {
        trackLineLabel(viewer, viewer.getPlotAreaMouseX());
        viewer.setAutoHide("all", "MouseOutPlotArea");
    });
});

//
// Draw track line with data labels
//
function trackLineLabel(viewer, mouseX)
{
    // Remove all previously drawn tracking object
    viewer.hideObj("all");

    // The chart and its plot area
    var c = viewer.getChart();
    var plotArea = c.getPlotArea();

    // Get the data x-value that is nearest to the mouse, and find its pixel coordinate.
    var xValue = c.getNearestXValue(mouseX);
    var xCoor = c.getXCoor(xValue);

    // Draw a vertical track line at the x-position
    viewer.drawVLine("trackLine", xCoor, plotArea.getTopY(), plotArea.getBottomY(), "black 1px dotted");

    // Draw a label on the x-axis to show the track line position
    viewer.showTextBox("xAxisLabel", xCoor, plotArea.getBottomY() + 4, JsChartViewer.Top,
        c.xAxis().getFormattedLabel(xValue, "mmm dd, yyyy"),
        "font:bold 11px Arial;color:#FFFFFF;background-color:#000000;padding:0px 3px");

    // Iterate through all layers to draw the data labels
    for (var i = 0; i < c.getLayerCount(); ++i)
    {
        var layer = c.getLayerByZ(i);

        // The data array index of the x-value
        var xIndex = layer.getXIndexOf(xValue);

        // Iterate through all the data sets in the layer
        for (var j = 0; j < layer.getDataSetCount(); ++j)
        {
            var dataSet = layer.getDataSetByZ(j);

            // Get the color and position of the data label
            var color = dataSet.getDataColor();
            var yCoor = c.getYCoor(dataSet.getPosition(xIndex), dataSet.getUseYAxis());

            // Draw a track dot with a label next to it for visible data points in the plot area
            if ((yCoor != null) && (yCoor >= plotArea.getTopY()) && (yCoor <= plotArea.getBottomY()) &&
                (color != null))
            {
                viewer.showTextBox("dataPoint" + i + "_" + j, xCoor, yCoor, JsChartViewer.Center,
                    viewer.htmlRect(7, 7, color));

                viewer.showTextBox("dataLabel" + i + "_" + j, xCoor + 5, yCoor, JsChartViewer.Left,
                    dataSet.getValue(xIndex).toPrecision(4),
                    "padding:0px 3px;font:bold 10px Arial;background-color:" + color + ";color:#FFFFFF");
            }
        }
    }
}

</script>
<div style="font-size:18pt; font-family:verdana; font-weight:bold">
    Track Line with Data Labels
</div>
<hr style="border:solid 1px #000080" />
<div style="font-size:10pt; font-family:verdana; margin-bottom:1.5em">
    <a href="viewsource.py?file=%(SCRIPT_NAME)s">View Source Code</a>
</div>
<!-- ****** Here is the chart image ****** -->
%(chartImg)s
</body>
</html>
""" % {
    "loadResource" : loadResource,
    "id" : viewer.getId(),
    "SCRIPT_NAME" : os.environ["SCRIPT_NAME"],
    "chartImg" : viewer.renderHTML()
    })

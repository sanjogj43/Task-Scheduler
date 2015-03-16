#!/usr/bin/python
import cgi, os

# Get HTTP query parameters
query = cgi.FieldStorage(keep_blank_values = 1)

print("Content-type: text/html\n")
print("""
<html>
<body style="margin:5px 0px 0px 5px">
<div style="font-size:18pt; font-family:verdana; font-weight:bold">
    Simple Clickable Pie Chart Handler
</div>
<hr style="border:solid 1px #000080" />
<div style="font-size:10pt; font-family:verdana; margin-bottom:20px">
    <a href="viewsource.py?file=%(SCRIPT_NAME)s">View Source Code</a>
</div>
<div style="font-size:10pt; font-family:verdana;">
<b>You have clicked on the following sector :</b><br />
<ul>
    <li>Sector Number : %(sector)s</li>
    <li>Sector Name : %(label)s</li>
    <li>Sector Value : %(value)s</li>
    <li>Sector Percentage : %(percent)s%%</li>
</ul>
</div>
</body>
</html>
""" % {
    "SCRIPT_NAME" : os.environ["SCRIPT_NAME"],
    "sector" : query["sector"].value,
    "label" : query["label"].value,
    "value" : query["value"].value,
    "percent" : query["percent"].value
    })

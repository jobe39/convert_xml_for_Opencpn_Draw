Simple Python File to convert gpx file from http://www.anchoragesincroatia.net/p/map-download.html for the OpenCPN draw plugin.

INSTALL:
========
Simply download the python file. Install Python interpreter, pip and install lxml library and needed dependences for lxml. 

HOW TO USE:
===========
Download the gpx file from above site. Rename it to "Import.gpx". Unfortunately the file contains some href tags, that could not be read by the xml parser. So you need to open the file in a text editor and replace all href=xxx....yyy.html by href="xxx....yyy.html" manualy (should already be corrected in the file, so probably not needed anymore). 

Put the Import.gpx file into the same directory where you have stored the python file. Run the python file and it should create a file called "Output.gpx" in the same directory. Now open OpenCPN - open the DRAW plugin - install the GPX file. Now you should see all anchorages within your map in OpenCPN.



Simple Python File to convert gpx file from http://www.anchoragesincroatia.net/p/map-download.html for the OpenCPN draw plugin.

Beta! 

USE WITH CARE - GUIDS for Points are created by this script. If you alread use the draw plugin, please check for your highest guid and change the value in the main function (starting point for incementing guids to be uploaded to OpenCPN draw)

INSTALL:
========
Simply download the python file. Install Python interpreter, pip and install lxml library. 

HOW TO USE:
===========
Download the gpx file from above site. Rename it to "Import.gpx". Unfortunately the file contains some href tags, that could not be read by the xml parser. So you need to open the file in a text editor and replace all href=xxx....yyy.html by href="xxx....yyy.html" manualy. There are only five or six of them.
Put the Import.gpx file into the same directory where you have stored the python file. Run the python file and it should create a file called "Output.gpx" in the same directory. Now open OpenCPN - open the DRAW plugin - install the GPX file. Now you should see all anchorages within your map in OpenCPN.



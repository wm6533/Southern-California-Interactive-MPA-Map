# Southern-California-Interactive-MPA-Map
A leaflet based web map of southern california oceans that has filterable marine protected areas as part of the map. 
Very much a work in progress, the end goal is to have a tile based map that has geojson polygons for each of the mpa's in SoCal,
with a UI that can filter by MPA type, fishing method allowed (hook and line vs spear and commercial vs recreational as examples),
and a color coded legend for the MPA types (either SMR or SMCA). 

You can run this project locally by using python's SimpleHTTPServer (assuming you have python installed), simply navigate to the repo's location on your drive in the cmd prompt
and type "python -m SimpleHTTPServer" to run, then navigate to http://127.0.0.1:8000 in any browser to view the map.

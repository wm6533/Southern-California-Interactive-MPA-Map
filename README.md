# Southern-California-Interactive-MPA-Map

THE GOAL
A leaflet based web map of southern california oceans that has filterable marine protected areas as part of the map. 
Very much a work in progress, the end goal is to have a tile based map that has geojson polygons for each of the mpa's in SoCal,
with a UI that can filter by MPA type, fishing method allowed (hook and line vs spear and commercial vs recreational as examples),
and a color coded legend for the MPA types (either SMR or SMCA).

WHY
Because the current tools to check MPA regulations are awful. Ideally this would let non technical people to view MPA regulations without having to comb through individual requirements on the DFG's website.


HOW TO RUN
You can run this project locally by using python's SimpleHTTPServer (assuming you have python installed).

In your command prompt and navigate to the repo's location.
Then type python -m SimpleHTTPServer in the command prompt.
If python is not recognized as a command, you need to update your environment path. 

From there, navigate to http://127.0.0.1:8000/sideproj.htm in any browser to view the map.

WHATS LEFT
Right now the project is a pretty map with color coded geojson polygons. It still needs
- a UI
- filterability
- interactivity


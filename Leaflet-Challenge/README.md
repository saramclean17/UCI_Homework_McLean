# Visualizing Data with Leaflet
Welcome to the United States Geological Survey, or USGS for short! The USGS is responsible for providing scientific data about natural hazards, the health of our ecosystems and environment; and the impacts of climate and land-use change. Their scientists develop new methods and tools to supply timely, relevant, and useful information about the Earth and its processes. As a new hire, you will be helping them out with an exciting new project!
The USGS is interested in building a new set of tools that will allow them visualize their earthquake data. They collect a massive amount of data from all over the world each day, but they lack a meaningful way of displaying it. Their hope is that being able to visualize their data will allow them to better educate the public and other government organizations (and hopefully secure more funding..) on issues facing our planet.

#Step 1--
#Basic Visualization.

The first step was to visualize an earthquake data set.
- The USGS provides earthquake data in a number of different formats, updated every 5 minutes.
- The "All Earthquakes from the Past 30 Days" data set was selected from the USGS GeoJSON Feed page.
- The data was given in JSON format which was used to pull in the data for the visualization.

#Import and Visualizing the Dataset

- I created a map using Leaflet that plots all of the earthquakes from the data set based on their longitude and latitude.
- The data markers reflect the magnitude of the earthquake by their size and and depth of the earth quake by color.
- Earthquakes with higher magnitudes appear larger and earthquakes with greater depth appear darker in color.
- Popups that provide additional information about the earthquake were included when a marker is clicked.
- A legend was created to provide context for the map data.

#Step 2--
#Adding more Data.

- I plotted a second data set on the map above to illustrate the relationship between tectonic plates and seismic activity.
- Then I pulled in the required Tectonic Plates data set.
- Then I visualized it along side the original set of data
- Next I added a number of base maps (Satellite Map, Grayscale Map, Outdoors Map and Dark Map) to choose from.
- Separated out the two different data sets (earthquakes and tectonic plates) into overlays that can be turned on and off independently.
- Finally layer controls were added to the map.

Copyright. Sara McLean. 2021 Trilogy Bootcamp

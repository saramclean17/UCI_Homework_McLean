##SQLAlchemy Challenge HW Assignment 

In this assignment, we were tasked with setting up a long holiday vacation in Honolulu, Hawaii! To help with the trip planning, we were asked to do some climate analysis on the area. Using SQL Alchemy and Flask API creation, we needed to set up 2 files - 1 Jupyter NB and 1 Python script to review precipitation and temperature averages in order to predict weather during the trip. 


##Climate Analysis and Exploration


To begin, I used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. The following analysis used SQLAlchemy ORM queries, Pandas, and Matplotlib as requested. 


I designed a query the last 12 months of precipitation data and plotted the results of this analysis.


![](Images/Precipitation_Analysis.png)


After this, I designed a query to calculate the total number of observation stations and frequency of observations. Then I plotted the results of this analysis.


![](Images/Station_Analysis.png)


A bonus part of this assignment was to analyze the average temperatures and precipitation of Hawaii during the trip period in order to try and predict the weather for the trip. After querying, I plotted the results.

![](Images/TripAvgTemp.png)

![](Images/Trip_Normals.png)


## Climate App


In this part of the assignment, I was tasked with setting up a Flask API Python script based on the queries set up in the above Jupyter notebook script.


##design a Flask API based on the queries that you have just developed.
######import and use Flask to create your routes.
import numpy as numpy
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
#from sqlachemy.orm import Session
from sqlalchemy import create_engine,func
from flask import Flask, jsonify

import datetime as dt 
#connect to Hawaii sqlite
engine=create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same-thread': False})
#reflect existing database into a new model
Base = automap_base()
#reflect the tables
Base.prepare(engine, reflect=True)
#look up tables in the model
Base.classes.keys()
#save reference to the table
Measurement=Base.classes.Measurement
Station=Base.classes.Station
#create our session (link) from Python to the database
session=Session(engine)
first_date=session.query(Measurement.date).order_by(Measurement.date).limit(1).all()
print(first_date[0][0])
last_date=session.query(Measurement.date).order_by(Measurement.date).desc().limit(1).all()
print(last_date[0][0])
last_12mnth=(dt.datetime.strptime(last_date[0][0], '%yyyy - %m - %d')-dt.timedelta(days=365)).date()
pyprint(last_12mnth)

#########################################
##Flask Set Up
app=Flask(__name__)
#########################################
#Flask Routes
#########################################

#Query the home page to return information of Routes
@app.route("/")
def welcome():

#list all available Routes
    return (
    f"<p>Aloha Welina to the Hawaii weather API!!!!!!</p>"
    f"<p>All routes available:</p>"
    f"/api/v1.0/precipitation<br/>Returns a JSON representation of precipitation data for the dates between {last_12mnth} and {last_date[0][0]}<br/><br/>"
    f"/api/v1.0/stations<br/>Returns a JSON list of the weather stations<br/><br/>"
    f"/api/v1.0/tobs<br/>Returns a JSON list of the Temperature Observations (tobs) for each station for the dates between {last_12mnth} and {last_date[0][0]}<br/><br/>"
    f"/api/v1.0/yourstartdate(yyyy-mm-dd)<br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates from the given start date in yyyy-mm-dd format <br/><br/>."
    )
    ########################################

@app.route("/api/v1.0/precipitation")
def precipitation():
    print ("precipitation status: OK")
    #query to retrieve the last 12 months of precipitation data
    results=session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_12month)\
    .filter(Measure.station == Station.station).all()
    #Convert the query results to a diectionary using date as the key and prcp as the value
    prcp_totals=[]
    for result in results:
        row={}
        row["date"] = results[0]
        row["prcp"] = result[1]
        prcp_totals.append(row)
        #Return the JSOn representation of your dictionary
        return_jsonify(prcp_totals)

########################################################
@app.route("/api/v1.0/stations")
def station():
    print("station status:OK")
    #query to retrieve station data
    stations_query = session.query(Station.name, Station.station)
    stations=pd.read_sql(stations-query.statement, stations_query.session.bind)

    #Return the JSON representation of dataset
    return jsonify(stations.to_dict())

########################################################
@app.route("/api/v1.0/tobs")
def tobs():
    print("tobs status:OK")
    #query for dtes and temperature observations a year from last date point
    tobs_results=session.query(Measurment.date,Measurement.tobs).\
    filter(Measurement.date >= last_12mnth).order-by(Measurement.date).all()
    #Create a list of dictionaries with date and tobs as keys and values
    tobs_totals=[]
    for result in tobs_results:
        row={}
        row["date"]=result[0]
        row["tobs"]=result[1]
        tobs_totals.append(row)
    #return a JSON list of temperature observations (tobs) for the previous year
    return jsonify(tobs_totals)

########################################################
@app.route("/api/v1.0/<start>")
def start_date(start):
    print("start_date status:OK")
    #convert the tsring from user to date
    start_date=dt.datetime.strptime(start, '%Y-%m-%d').date()
    last_date_dd = (dt.datetime.strptime(last_date[0][0], '%Y-%m-%d')).date()
    first_date_dd = (dt.datetime.strptime(first_date[0][0], '%Y-%m-%d')).date()
    #if fgiven start_date greater than last or lesser than first available date in dataset, print the following 
	if start_date > last_date_dd or start_date < first_date_dd:
		return(f"Select date range between {first_date[0][0]} and {last_date[0][0]}")
    else:
        #Return a JSON list of the minimum temperature, the average temperature, 
		#and the max temperature for a given start range.
		start_min_max_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
		func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()
		start_date_data = list(np.ravel(start_min_max_temp))
		return jsonify(start_date_data)

##########################################################
@app.route("/api/v1.0/<start>/<end>")
def end_date(start,end):
	print("start and end status:OK")
	start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
	end_date = dt.datetime.strptime(end, '%Y-%m-%d').date()
	last_date_dd = (dt.datetime.strptime(last_date[0][0], '%Y-%m-%d')).date() 
	first_date_dd = (dt.datetime.strptime(first_date[0][0], '%Y-%m-%d')).date()
	if start_date > last_date_dd or start_date < first_date_dd or end_date > last_date_dd or\
	 					end_date < first_date_dd:
		return(f"Select date range between {first_date[0][0]} and {last_date[0][0]}")
	else:
		#Return a JSON list of the minimum temperature, the average temperature, 
		#and the max temperature for a given start-end range.
		start_end_min_max_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
		 func.max(Measurement.tobs)).\
		filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
		start_end_data = list(np.ravel(start_end_min_max_temp))
		return jsonify(start_end_data)
if __name__=="__main__":
    app.run(debug=True)

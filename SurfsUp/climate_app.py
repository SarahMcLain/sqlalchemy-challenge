# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../sqlalchemy-challenge/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session= Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )
#route for precipitation query results of the last 12 months. Create dictionary  
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

    session.close()

    precipitation = {date: prcp for date, prcp in results}

    return jsonify(precipitation)

#Route for stations in the data set
@app.route("/api/v1.0/stations")
def stations():
    
    """Return a list of all stations names"""
    # Query all stations
    results = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

#Route for most active stations
@app.route("/api/v1.0/tobs")
def tobs():
    results = session.query(func.min(Measurement.tobs), 
                                         func.max(Measurement.tobs), 
                                         func.avg(Measurement.tobs)).filter(Measurement.station == 'USC00519281').all()
    session.close()

    top_active_station = list(np.ravel(results))

    return jsonify(top_active_station)

#Route for min, max, avg temps in a specified start and end date format 'YYYY-MM-DD'
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temps_at_start(start = None, end = None):
    
    select = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    if not end:
        start = dt.datetime.strptime(start, "%Y-%m-%d").date()
        results = session.query(*select).filter(Measurement.date >= start).all() 
        session.close()
        
        query_results = list(np.ravel(results))
        return(query_results)

    start = dt.datetime.strptime(start, "%Y-%m-%d").date()
    end = dt.datetime.strptime(end, "%Y-%m-%d").date()
    results = session.query(*select).filter(Measurement.date <= end).all() 
    session.close()
            
    query_results = list(np.ravel(results))
    return(query_results)
            
 
#Run program as main program and enable debugging    
if __name__ == '__main__':
    app.run(debug=True)







# sqlalchemy-challenge

        Jupyter notebook code

Setting up your notebook:
    This notebook is designed to use python and SQLALchemy to explore climate data. 

    First import sqlalchemy, automap_base from sqlalchemy.ext.automap, Session from sqlalchemy.orm, and create_engine, inspect, func from sqlalchemy 

    Create engine and refelct database into a new model (autolaod_with=engine)

    Save references to tables as variables

    Create a session link

Analysis of Precipitation: 
    Query to find the most recent date in dataset and then find the previous 12 months of data.

    Create a dataframe and set the column names; generate bar plot for dataset. 

Analysis of Stations:
    Calculate total number of stations in the dataset and then order the data from most active station to least.

    Find the min, max, and avg temperatures from the most active station. 

Analysis of 12-months data:
    Query the previous 12 months of temperature data filtered by the most active station.
    Plot histogram of results  
Close Session 

        Climate App Code

Create app to hold results of jupyter notebook query finds. 
   @app.route("/") Welcome page
   @app.route("/api/v1.0/precipitation") Precipitation query
   @app.route("/api/v1.0/stations") Active station query
   @app.route("/api/v1.0/tobs") tobs query
   @app.route("/api/v1.0/<start>") tobs query for specified dates 
    @app.route("/api/v1.0/<start>/<end>")





from flask import Flask, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import datetime as dt
from sqlalchemy import func, FLOAT
import numpy as np

#################################################
# Database Setup
engine = create_engine("sqlite:///../Resources/hawaii.sqlite", echo=False)
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
M = Base.classes.measurement
S = Base.classes.station
#################################################


#################################################
# Flask Setup
app = Flask(__name__)
#################################################


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/range/2012-02-23<br/>"
        f"/api/v1.0/range/2016-8-23/2017-8-23"

    )

@app.route("/api/v1.0/precipitation")
def get_climate():
    session = Session(engine)
    start_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(M.date, M.prcp).\
        filter(M.date >= start_date).all()
    session.close()

    # Create a dictionary 
    date_dict = {}
    for date, prcp in results:
        date_dict[date] = prcp

    return jsonify(date_dict)

@app.route("/api/v1.0/stations")
def get_station():
    session = Session(engine)
    results = session.query(S.station).distinct().all()
    session.close()

    #  # Create a dictionary 
    # all_stations = []
    # for station in results:
    #     station_dict = {}
    #     station_dict["station"] = station
    #     all_stations.append(station_dict)

    #print(all_stations)
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def get_tobs():
    session = Session(engine)
    start_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(M.date, M.tobs).\
    filter(M.station == 'USC00519281').filter(M.date >= start_date).all()
    session.close()

    # Create a dictionary 
    all_tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)

@app.route("/api/v1.0/range/<start>")
def get_start(start):
    session = Session(engine)
    starter_date = start.replace(" ", "").lower()

    results = session.query(func.min(M.tobs), func.max(M.tobs), func.avg(M.tobs)).\
    filter(M.date >= starter_date).all()
    session.close()

    date_results = list(np.ravel(results))
    return jsonify(date_results)

@app.route("/api/v1.0/range/<start>")   
@app.route("/api/v1.0/range/<start>/<end>")
def get_dates(start=None, end=None):
    session = Session(engine)
    start_date = start.replace(" ", "").lower()
    end_date = end.replace(" ", "").lower()

    range_results = session.query(M.date, func.min(M.tobs), func.max(M.tobs), func.avg(M.tobs)).\
    filter(M.date >= start_date and M.date <= end_date).all()
    session.close()

    final_results = list(np.ravel(range_results))
    return jsonify(final_results)   



if __name__ == '__main__':
    app.run(debug=True)
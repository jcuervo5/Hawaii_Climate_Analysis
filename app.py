import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

database_path = "Resources/hawaii.sqlite"
engine = create_engine(f"sqlite:///{database_path}")

Base = automap_base()

Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)


@app.route("/")
def index():
    return(
        f"Home Page<br><br>"
        f"Available Routes:<br><br>"
        f"/api/v1.0/precipitation<br><br>"
        f"/api/v1.0/stations<br><br>"
        f"/api/v1.0/tobs<br><br>"
        f"/api/v1.0/"
        f"insert start date<br><br>"
        f"/api/v1.0/"
        f"insert start date/insert end date<br><br>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    query_date = dt.date(2017, 8, 23) - dt.timedelta(weeks=52)

    results = session.query(measurement.date,measurement.prcp).\
        filter(measurement.date >= query_date).\
        order_by(measurement.date).all()

    session.close()

    # query_results = list(np.ravel(results))

    return jsonify(results)
    
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    stations = session.query(station.station).all()
        
    session.close()

    # stations_list = list(np.ravel(stations))

    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    query_date = dt.date(2017, 8, 23) - dt.timedelta(weeks=52)

    station_temp = session.query(measurement.date,measurement.tobs).\
        filter(measurement.station == 'USC00519281').\
        filter(measurement.date >= query_date).\
        order_by(measurement.date.desc()).all()

    session.close()

    tobs_list = list(np.ravel(station_temp))

    return jsonify(tobs_list)


@app.route("/api/v1.0/<start>")
def start_date(start):
    session = Session(engine)

    tmax = session.query(func.max(measurement.tobs)).\
        filter(measurement.date == start).all()

    tmin = session.query(func.min(measurement.tobs)).\
        filter(measurement.date == start).all()

    tavg = session.query(func.avg(measurement.tobs)).\
        filter(measurement.date == start).all()

    return (
        f'Temperature information for: {start}<br><br>'
        f'Max Temperature: {tmax}<br><br>'
        f'Min Temperature: {tmin}<br><br>'
        f'Avg Temperature: {tavg}'
    )

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)

    tmax = session.query(func.max(measurement.tobs)).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).all()

    tmin = session.query(func.min(measurement.tobs)).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).all()

    tavg = session.query(func.avg(measurement.tobs)).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).all()

    return (
        f'Temperature information for: {start} through {end}<br><br>'
        f'Max Temperature: {tmax}<br><br>'
        f'Min Temperature: {tmin}<br><br>'
        f'Avg Temperature: {tavg}'
    )

# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
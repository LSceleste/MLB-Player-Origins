import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///baseball.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
BaseballPlayers = Base.classes.baseball

# Create our session (link) from Python to the DB
session = Session(engine)

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
        f"/api/v1.0/birthcity<br/>"
        f"/api/v1.0/latlng"
    )

@app.route("/api/v1.0/birthcity")
def lats():
    """Return a list of all birthcity"""
    # Query all lats
    results = session.query(BaseballPlayers.birthCity).all()

    # Convert list of tuples into normal list
    all_birthCity = list(np.ravel(results))

    return jsonify(all_birthCity)

@app.route("/api/v1.0/latlng")
def latlng():
    """Return a list of playerstats including latitude, longitude"""
    # Query all latlngs
    results = session.query(BaseballPlayers.latitude, BaseballPlayers.longitude).all()

    # Create a dictionary from the row data and append to a list of all_latlngs
    all_latlng = []
    for latitude, longitude in results:
        stats_dict = {}
        stats_dict["latitude"] = latitude
        stats_dict["longitude"] = longitude
        all_latlng.append(stats_dict)

    return jsonify(all_latlng)

if __name__ == '__main__':
    app.run(debug=True)






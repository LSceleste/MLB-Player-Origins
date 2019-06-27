import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/baseball.sqlite"

db = SQLAlchemy(app)


# Create our database model
class Baseball(db.Model):
    __tablename__ = 'baseball'

    id = db.Column(db.Integer, primary_key=True)
    birthYear = db.Column(db.Integer)
    nameFirst = db.Column(db.String)
    nameLast = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return '<Baseball %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index2.html")


@app.route("/birthYear")
def stats_data():
    """Return birthYear"""
    #get entire table, and print everything using "results"
    #match return (result) with original csv to see if everything will print
    # Query for the top 10 emoji data
    results = db.session.query(Baseball.birthYear, Baseball.nameFirst, Baseball.nameLast, Baseball.latitude, Baseball.longitude).\
        order_by(Baseball.birthYear.desc()).\
        limit(10).all()

    # Create lists from the query results
    nameLast = [result[0] for result in results]
    birthYear = [result[1] for result in results]
    print(results)
    # # Generate the plot trace
    trace = {
        "x": nameLast,
        "y": birthYear,
        "type": "bar"
    }
    return jsonify(results)


# @app.route("/emoji_id")
# def emoji_id_data():
#     """Return emoji score and emoji id"""

#     # Query for the emoji data using pandas
#     query_statement = db.session.query(Emoji).\
#         order_by(Emoji.score.desc()).\
#         limit(10).statement
#     df = pd.read_sql_query(query_statement, db.session.bind)

#     # Format the data for Plotly
#     trace = {
#         "x": df["emoji_id"].values.tolist(),
#         "y": df["score"].values.tolist(),
#         "type": "bar"
#     }
#     return jsonify(trace)


# @app.route("/emoji_name")
# def emoji_name_data():
#     """Return emoji score and emoji name"""

#     # Query for the top 10 emoji data
#     results = db.session.query(Emoji.name, Emoji.score).\
#         order_by(Emoji.score.desc()).\
#         limit(10).all()
#     df = pd.DataFrame(results, columns=['name', 'score'])

#     # Format the data for Plotly
#     plot_trace = {
#         "x": df["name"].values.tolist(),
#         "y": df["score"].values.tolist(),
#         "type": "bar"
#     }
#     return jsonify(plot_trace)


if __name__ == '__main__':
    app.run(debug=True)



















# import numpy as np

# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func

# from flask import Flask, jsonify


# #################################################
# # Database Setup
# #################################################
# engine = create_engine("sqlite:///baseball.sqlite")

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# # Save reference to the table
# BaseballPlayers = Base.classes.baseball

# # Create our session (link) from Python to the DB
# session = Session(engine)

# #################################################
# # Flask Setup
# #################################################
# app = Flask(__name__)


# #################################################
# # Flask Routes
# #################################################

# @app.route("/")
# def welcome():
#     """List all available api routes."""
#     return (
#         f"Available Routes:<br/>"
#         f"/api/v1.0/birthcity<br/>"
#         f"/api/v1.0/latlng"
#     )

# @app.route("/api/v1.0/birthcity")
# def lats():
#     """Return a list of all birthcity"""
#     # Query all lats
#     results = session.query(BaseballPlayers.birthCity).all()

#     # Convert list of tuples into normal list
#     all_birthCity = list(np.ravel(results))

#     return jsonify(all_birthCity)

# @app.route("/api/v1.0/latlng")
# def latlng():
#     """Return a list of playerstats including latitude, longitude"""
#     # Query all latlngs
#     results = session.query(BaseballPlayers.latitude, BaseballPlayers.longitude).all()

#     # Create a dictionary from the row data and append to a list of all_latlngs
#     all_latlng = []
#     for latitude, longitude in results:
#         stats_dict = {}
#         stats_dict["latitude"] = latitude
#         stats_dict["longitude"] = longitude
#         all_latlng.append(stats_dict)

#     return jsonify(all_latlng)

# if __name__ == '__main__':
#     app.run(debug=True)






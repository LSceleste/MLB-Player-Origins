import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/baseball.sqlite"
app.config['SQLALCHEMY_BINDS'] = {
        'combined_db':"sqlite:///db/baseballDeath.sqlite"
}

db = SQLAlchemy(app)

class BaseballDeath(db.Model):
    __bind_key__ = 'combined_db'
    __tablename__= 'final2'
    
    id = db.Column(db.Integer, primary_key=True)
    birthYear = db.Column(db.Integer)
    nameFirst = db.Column(db.String)
    nameLast = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    country_iso_code = db.Column(db.String)
    deathYear = db.Column(db.Integer)
    birthCity = db.Column(db.String)
    flags = db.Column(db.String)
    deathCity = db.Column(db.String)
    deathCountry = db.Column(db.String)

    def __repr__(self):
        return '<Baseball2 %r>' % (self.name)
# Create our database model
class Baseball(db.Model):
    __tablename__ = 'final'

    id = db.Column(db.Integer, primary_key=True)
    birthYear = db.Column(db.Integer)
    nameFirst = db.Column(db.String)
    nameLast = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    country_iso_code = db.Column(db.String)
    deathYear = db.Column(db.Integer)
    birthCity = db.Column(db.String)
    flags = db.Column(db.String)
    deathCity = db.Column(db.String)
    deathCountry = db.Column(db.String)
    

    def __repr__(self):
        return '<Baseball %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():
<<<<<<< HEAD
    print("set up")# Recreate database each time for demo
    # db.drop_all()
=======
>>>>>>> f50d5dc9613c083685de5799f9c9821938619362
    db.create_all()
    db.create_all(bind='combined_db')


@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


@app.route("/birthYear")
def stats_data():
    """Return birthYear"""
    #get entire table, and print everything using "results"
    #match return (result) with original csv to see if everything will print
    # Query for the necessary data
    results = db.session.query(Baseball.birthYear, Baseball.nameFirst, Baseball.nameLast, 
        Baseball.latitude, Baseball.longitude, Baseball.country_iso_code, Baseball.deathYear,
        Baseball.birthCity, Baseball.flags, Baseball.deathCity, Baseball.deathCountry).\
        order_by(Baseball.birthYear.desc()).\
        limit(20000).all()

    # Create lists from the query results
    nameLast = [result[0] for result in results]
    birthYear = [result[1] for result in results]
    nameFirst = [result[2] for result in results]
    latitude = [result[3] for result in results]
    longitude = [result[4] for result in results]
    country_iso_code = [result[5] for result in results]
    deathYear = [result[6] for result in results]
    birthCity = [result[7] for result in results]
    flags = [result[8] for result in results]
    deathCity = [result[9] for result in results]
    deathCountry = [result[10] for result in results]
    
    
    return jsonify(results)

@app.route("/deathYear")
def stats_data2():
    """Return deathYear"""
    #get entire table, and print everything using "results"
    #match return (result) with original csv to see if everything will print
    # Query for the necessary data
    results2 = db.session.query(BaseballDeath.birthYear, BaseballDeath.nameFirst, BaseballDeath.nameLast, 
        BaseballDeath.latitude, BaseballDeath.longitude, BaseballDeath.country_iso_code, BaseballDeath.deathYear,
        BaseballDeath.flags, BaseballDeath.deathCity, BaseballDeath.deathCountry).\
        order_by(BaseballDeath.deathYear.desc()).\
        limit(20000).all()

    # Create lists from the query results
    nameLast = [result[0] for result in results2]
    birthYear = [result[1] for result in results2]
    nameFirst = [result[2] for result in results2]
    latitude = [result[3] for result in results2]
    longitude = [result[4] for result in results2]
    country_iso_code = [result[5] for result in results2]
    deathYear = [result[6] for result in results2]
<<<<<<< HEAD
    flags = [result[7] for result in results2]
    deathCity = [result[8] for result in results2]
    deathCountry = [result[9] for result in results2]
    
    # # Generate the plot trace
    # trace = {
    #     "x": nameLast,
    #     "y": birthYear,
    #     "type": "bar"
=======
    birthCity = [result[7] for result in results2]
    flags = [result[8] for result in results2]
    deathCity = [result[9] for result in results2]
    deathCountry = [result[10] for result in results2]
    
    print(results2)
>>>>>>> f50d5dc9613c083685de5799f9c9821938619362
    
    return jsonify(results2)

@app.route("/sources")
def sources():
    """Render Home Page."""
    return render_template("sources.html")


if __name__ == '__main__':
    app.run(debug=True)
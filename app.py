from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars as sm

app=Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)
# conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
# client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
# db = client.mars_db

# Drops collection if available to remove duplicates
# db.mars_info.drop()

@app.route("/")
def index():

    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    
    mars= mongo.db.mars
    mars_data=sm.scrape_all()
    mars.update({},mars_data,upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


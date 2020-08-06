######################
# Import dependencies
######################

from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

############################
# Configure Flask and Mongo
############################

app = Flask(__name__)
conn = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(conn)
mars_db = client.mars_db
mars_collection = mars_db.mars_collection

####################
# Configure routes
####################

@app.route("/scrape")
def scrape_new_data():
    mars_dict = scrape_mars.scrape()
    mars_collection.update({}, mars_dict, upsert=True)
    return "Scrape Complete"

@app.route("/")
def home():
    mars_collection = mongo.db.mars.find_one()
    return render_template("index.html", mars_collection=mars_collection)

if __name__ == "__main__":
    app.run()




######################
# Import dependencies
######################

from flask import Flask, render_template
import scrape_mars
import pymongo

############################
# Configure Flask and Mongo
############################

app = Flask(__name__)
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars_db
mars_collection = db.items

####################
# Configure routes
####################

@app.route("/")
def home():
    mars_collection = db.items.find_one()
    return render_template("index.html", mars_collection=mars_collection)

@app.route("/scrape")
def scrape_new_data():
    mars_dict = scrape_mars.scrape()
    mars_collection.update({}, mars_dict, upsert=True)
    return "Scraping complete. Hit the back button to view results!"


if __name__ == '__main__':
    app.run(debug=False)




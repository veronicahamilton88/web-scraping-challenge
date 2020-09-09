from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars



# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route('/')
def index():
    mars = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars)

@app.route('/scrape')
def scrape():
    # mars = mongo.db.mars
    data = scrape_mars.scrape_info()
    mongo.db.collection.update(
        {},
        data,
        upsert=True
    )
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)



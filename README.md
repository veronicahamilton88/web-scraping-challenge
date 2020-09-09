# web-scraping-challenge
By: Veronica Hamilton

When accessing the Missions to Mars app, various different scientific websites will be visited and scraped for data.
This data is displayed in the index.html page, showing several different images and facts about Mars.
This is accomplished by using a combination of Flask, MongoDB, Splinter, BeautifulSoup, Pandas, and Python.

******

First, I created the mission_to_mars Python notebook to create and test my scraping code.
Each website that contains data we want to use, is visited within the Chrome Browser. BeautifulSoup then scrapes the page for the specified data. The scrapes are added to a Python dictionary for use in Flask later.

Next, I converted this notebook into the scrape_mars.py application.
I set up constructors 'init_browser' and 'scrape_info' which allows each of these classes to initialize within the app.
The init_browser class holds the path to our browser function from the notebook in step 1. The scrape_info class holds the rest of the scraping info from the notebook.
I added a line of code that will close the browser when scraping is finished, and then returned the mars function.

Then I constructed the app.py application.
This pushes the scrape into a mongoDB database so that the info can be stored.
Using flask I set up two routes for the index.html site that displays the data. The index route is the homepage. It also renders the template for our page. The /scrape route will run our scrape_mars application, and updates the database.
When finished it directs to the homepage.

Finally, I created the index.html file which displays all our data.
This includes a button to run the /scrape function to update the data in realtime. I also used Bootstrap to create a more aesthetic appearance of the page.
I integrated Flask with the HTML to call specific parts of that mongoDB database I created in order to display it on the page appropriately.

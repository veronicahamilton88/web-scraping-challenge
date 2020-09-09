import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import os

mars = {}

def init_browser():
    executable_path = {"executable_path": "C:/Users/Veron/OneDrive/Desktop/BUTLER_BOOTCAMP/drivers/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    # Provide the Mars News URL
    mars_news_url = "https://mars.nasa.gov/news/"

    browser.visit(mars_news_url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    mars_news_soup = bs(html, "html.parser")

    # Get the most recent news title
    news_title = mars_news_soup.find_all('div', class_='content_title')
    mars["news_title"]=news_title[1].text

    # Get the most recent news paragraph
    news_p = mars_news_soup.find('div', class_='article_teaser_body')
    mars["news_p"]=news_p.text


    # Pass the space images URL
    space_images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(space_images_url)

    #Click into the full size images
    browser.find_by_id("full_image").click()
    time.sleep(1)
    browser.links.find_by_partial_text("more info").click()
    time.sleep(1)
    
    # Scrape page into Soup
    html = browser.html
    mars_news_soup = bs(html, "html.parser")

    result = mars_news_soup.find('figure', class_="lede")
    link=result.a.img["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + link
    mars["featured_image"] = featured_image_url


    space_facts_url = "https://space-facts.com/mars/"
    browser.visit(space_facts_url)
    # Scrape page into Soup
    html = browser.html
    mars_facts_soup = bs(html, "html.parser")

    table=pd.read_html(space_facts_url)
    df=table[0]
    df.columns=['Description', 'Value']
    html_table=df.to_html()
    html_table=html_table.replace('\n', '')
    mars["facts"] = html_table


    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)

    hemisphere_image_url=[]
    links = browser.find_by_css("a.product-item h3")
    for link in range(len(links)):
        hemispheres={}
        browser.find_by_css("a.product-item h3")[link].click()
        element = browser.find_link_by_text('Sample').first
        hemispheres["img_url"]=element["href"]
        hemispheres["title"]=browser.find_by_css("h2.title").text
        hemisphere_image_url.append(hemispheres)
        browser.back()
        mars["hemisphere"] = hemisphere_image_url
    
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars

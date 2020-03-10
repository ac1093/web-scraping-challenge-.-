from splinter import Browser
from bs4 import BeautifulSoup
from splinter import Browser
import pymongo
import requests
import pandas as pd

mars_dict = {}

def init_browser():

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)
def news_scrape():

    url = 'https://mars.nasa.gov/news/'
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.nasa_db
    collection = db.articles

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    headline = soup.find('div', class_ = 'content_title').find('a').text
    body = soup.find('div', class_ = 'rollover_description_inner').text
    
    mars_dict['headline'] = headline
    mars_dict['body'] = body
    
    return mars_dict

def scrape_img():
   Browser = init_browser()
   url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
   Browser.visit(url)
   html = browser.html
   soup = BeautifulSoup(html, 'html.parser')

   image_url = soup.find('footer').find('a')['data-fancybox-href']

   featured_image_url = f'https://www.jpl.nasa.gov{image_url}'
    
   mars_dict['featured_image_url'] = featured_image_url
   
   Browser.quit()
   return mars_dict


#twitter_url = 'https://twitter.com/marswxreport?lang=en'
#Browser.visit(twitter_url)
#html = Browser.html
#soup = BeautifulSoup(html, 'html.parser')

def mars_facts():
   Browser = init_browser()

   url = 'https://space-facts.com/mars/'
    
   Browser.visit(url)

   mars_df = pd.read_html(url)[2]
   mars_df.columns = ['Description', 'Value']

   mars_df_html = mars_df.to_html()
   Browser.quit()
   return mars_dict

#url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#Browser.visit(url)

#html = Browser.html
#soup = BeautifulSoup(html, 'html.parser')


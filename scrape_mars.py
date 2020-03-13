from splinter import Browser
from bs4 import BeautifulSoup
from splinter import Browser
import pymongo
import requests
import pandas as pd

mars_dict = {}

#def init_browser():

executable_path = {'executable_path': 'chromedriver'}
    #return 
Browser('chrome', **executable_path, headless=False)
def scrape():

    url = 'https://mars.nasa.gov/news/'
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = mars_db

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    headline = soup.find('div', class_ = 'content_title').find('a').text
    body = soup.find('div', class_ = 'rollover_description_inner').text

    mars_dict['headline'] = headline
    mars_dict['body'] = body
    Browser = init_browser()   
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    Browser.visit(url)
    html = Browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_url = soup.find('footer').find('a')['data-fancybox-href']

    featured_image_url = f'https://www.jpl.nasa.gov{image_url}'

    mars_dict['featured_image_url'] = featured_image_url

    Browser.quit()


            #twitter_url = 'https://twitter.com/marswxreport?lang=en'
            #Browser.visit(twitter_url)
            #html = Browser.html
            #soup = BeautifulSoup(html, 'html.parser')
    Browser = init_browser()

    url = 'https://space-facts.com/mars/'

    Browser.visit(url)

    mars_df = pd.read_html(url)[2]
    mars_df.columns = ['Description', 'Value']

    mars_df_html = mars_df.to_html()

    mars_dict['html'] = mars_df_html

    Browser.quit()
        #return mars_dict

    executable_path = {'executable_path': 'chromedriver.exe'}
    Browser = Browser('chrome', **executable_path, headless=False)

    url2 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    Browser.visit(url2)
    mars_dict=[]
            
    html = Browser.html
    soup = BeautifulSoup(html, 'html.parser')

    for x in range (4):

        print('hi')
        hemispheres = Browser.find_by_tag('h3')

                    
        hemispheres[x].click()

                    
        html = Browser.html
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find('h2',class_='title').text
        img = soup.find('img', class_='wide-image')['src']

                        
        img_url = f'https://astrogeology.usgs.gov{img}'

                        
        mars_dict.append({'title':title, 'hemishpere_url':img_url})

        Browser.quit()
    return mars_dict

print(mars_dict)
    
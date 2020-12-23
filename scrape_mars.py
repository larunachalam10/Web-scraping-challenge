

from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import os
import datetime as dt
import time

def init_browser():
    
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


#SCRAPPING MARS NEWS------------
def news():

    browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')

    content = soup.find_all('div', class_='content_title')
    news_title=content[1].text
    content1=soup.find_all('div',class_='article_teaser_body')
    paragraph=content1[0].text
    
    browser.quit()
    
    return news_title, paragraph

#JPL MARS SPACE IMAGE - FEATURED IMAGE

def featured_image():

    browser = init_browser()

    url1 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars#submit"
    browser.visit(url1)

    full_image=browser.find_by_id("full_image")
    full_image.click()

    browser.is_element_present_by_text("more info", wait_time=1)
    more_info=browser.find_link_by_partial_text("more info")
    more_info.click()

    html = browser.html
    image_soup = bs(html, 'html.parser')
    img=image_soup.find("figure", class_="lede")
    featured_image_url= 'https://www.jpl.nasa.gov' +(img.find('a').get('href'))
    browser.quit()

    return featured_image_url


#MARS FACTS ----------------

def mars_facts():

    browser = init_browser()

    url2 = "https://space-facts.com/mars/"
    
    browser.visit(url2)
    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')

    table = pd.read_html(url2)
    df=table[0]
    df.columns=['Description','Value']

    mars_html= df.to_html(table_id = "html_tbl_css", justify='left', index=False)
    browser.quit()

    return mars_html


#MARS HEMISPHERE----------------

def mars_hemisphere():

    browser= init_browser()

    url3="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url3)

    time.sleep(3)

    html=browser.html
    soup=bs(html, 'html.parser')
        
    desc= soup.find_all("div",class_="item")
    main_url="https://astrogeology.usgs.gov"
    hemispheres = []

    for  i in desc:
        post = {}
        post['title'] = (i.find('h3').text)
        partial_link=i.find('a',class_="itemLink product-item")['href']
        browser.visit(main_url + partial_link)
        time.sleep(3)
        partial_img_html=browser.html
        soup1=bs(partial_img_html,"html.parser")
        post['img_url'] = (main_url + soup1.find('img',class_='wide-image')['src'])
        hemispheres.append(post)

    return hemispheres

#----SCRAPE ALL THE DATA -------

def scrape_all():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)
    news_title, news_paragraph = news()
    img_url = featured_image()
    facts = mars_facts()
    hemisphere_image_urls = mars_hemisphere()
    timestamp = dt.datetime.now()

    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": img_url,
        "facts": facts,
        "hemispheres": hemisphere_image_urls,
        "last_modified": timestamp
    }
    browser.quit()

    return data 






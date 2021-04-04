import pandas as pd
import time
import requests
import os
import pymongo 
from bs4 import BeautifulSoup as bs
from splinter import Browser 
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # NASA MARS NEWS

    # Document url - need for Mars Planet Science website 
    mars_news_site = "https://redplanetscience.com/"

    # Browser to launch 
    browser.visit(mars_news_site)

    # Sleep - allowing time for data to load 
    time.sleep(1)

    # Scrape page into Soup
    mars_news_site = browser.html
    soup = bs(mars_news_site, "lxml")

    # Get the latest news title 
    news_title = soup.find("div", class_="content_title").text

    # Get the latest paragraph 
    paragraph_text = soup.find("div", class_="article_teaser_body").text

    # Get the max avg temp
    print(f"Paragraph:\n\n{paragraph_text}")


    # JPL MARS SPACE IMAGES - FEATURED IMAGE

    # Document url - need for Jet Propulsion Laboratory 
    jpl_images_site = "https://spaceimages-mars.com/"
    browser.visit(jpl_images_site)

    # Sleep - allowing time for data to load 
    time.sleep(1)

    jpl_image = browser.html
    soup = bs(jpl_image, "html.parser") 

    jpl_soup = soup.find("img", class_="headerimage")["src"]

    jpl_images_site + jpl_soup 

    featured_image_url = jpl_images_site + jpl_soup 
    featured_image_url






















    mars_info_html_table = []
    hemi_dicts = []
      # Store data in a dictionary
    scraped_data = {
        "news_title": news_title,
        "paragraph_text": paragraph_text,
        "featured_image_url": featured_image_url, 
        "mars_info_html_table": mars_info_html_table,
        "hemi_dicts": hemi_dicts
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return scraped_data

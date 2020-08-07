######################
# Import dependencies
######################

from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
import time

#########################
# Define scrape function
#########################

def scrape():
    
    ########################
    # Scrape Mars news data
    ########################

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    time.sleep(5)
    news_html = browser.html
    news_soup = BeautifulSoup(news_html, "html.parser")
    browser.quit()
    
    ############################
    # Locate Mars news headline
    ############################    
    
    news_title = news_soup.find_all("div", class_ = "content_title")[1].text
    
    #############################
    # Locate Mars news paragraph
    #############################
    
    news_paragraph = news_soup.find_all("div", class_ = "article_teaser_body")[0].text
    
    #########################
    # Scrape Mars image data
    #########################
    
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    time.sleep(5)
    image_html = browser.html
    image_soup = BeautifulSoup(image_html, "html.parser")
    browser.quit()
    
    #############################
    # Locate Mars featured image
    #############################
    
    image_results = image_soup.find_all("div", class_="carousel_container")
    for image_result in image_results:
        articles = image_result.find("article", class_="carousel_item")
        image_url_suffix = articles.a["data-fancybox-href"]
    image_base_url = "https://www.jpl.nasa.gov"
    image_url = image_base_url + image_url_suffix
    
    ###########################
    # Scrape Mars Twitter data
    ###########################
    
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)
    time.sleep(5)
    twitter_html = browser.html
    twitter_soup = BeautifulSoup(twitter_html, "html.parser")
    browser.quit()
    
    ###########################
    # Locate latest Mars tweet
    ###########################
    
    all_tweets = twitter_soup.find_all("span")
    for i in range(len(all_tweets)):
        if ("InSight" in all_tweets[i].text):
            latest_tweet = all_tweets[i].text
            break

    #########################
    # Scrape Mars facts data
    #########################
    
    facts_url = "https://space-facts.com/mars/"
    facts_response = requests.get(facts_url)
    facts_soup = BeautifulSoup(facts_response.text, "html.parser")
    
    #####################################
    # Locate Mars facts and create table
    #####################################
    
    facts_url = "https://space-facts.com/mars/"
    facts_table = pd.read_html(facts_response.text)
    facts_table_df = facts_table[0]
    facts_table_df.columns = ["Data Categories", "Mars Data"]
    facts_table_df.set_index("Data Categories", inplace = True)
    html_facts_table = facts_table_df.to_html()
    html_facts_table = html_facts_table.rstrip("/n")
    
    #######################################
    # Scrape Mars Cerberus Hemisphere data
    #######################################
    
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(cerberus_url)
    time.sleep(5)
    cerberus_html = browser.html
    cerberus_soup = BeautifulSoup(cerberus_html, "html.parser")
    browser.quit()
    
    ##################################################
    # Locate Mars Cerberus Hemisphere image and title
    ##################################################

    cerberus_url_results = cerberus_soup.find_all("li")
    cerberus_url_list = []
    for cerberus_url_result in cerberus_url_results:
        cerberus_urls = cerberus_url_result.find("a")["href"]
        cerberus_url_list.append(cerberus_urls)
    cerberus_url = cerberus_url_list[0]
    cerberus_title_results = cerberus_soup.find_all("h2", class_="title")
    cerberus_title_list = []
    for cerberus_title_result in cerberus_title_results:
        cerberus_titles = cerberus_title_result.text
        cerberus_title_list.append(cerberus_titles)
    cerberus_title = cerberus_title_list[0]
    
    ###########################################
    # Scrape Mars Schiaparelli Hemisphere data
    ###########################################
    
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    schiaparelli_url ="https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(schiaparelli_url)
    time.sleep(5)
    schiaparelli_html = browser.html
    schiaparelli_soup = BeautifulSoup(schiaparelli_html, "html.parser")
    browser.quit()
    
    ######################################################
    # Locate Mars Schiaparelli Hemisphere image and title
    ######################################################

    schiaparelli_url_results = schiaparelli_soup.find_all("li")
    schiaparelli_url_list = []
    for schiaparelli_url_result in schiaparelli_url_results:
        schiaparelli_urls = schiaparelli_url_result.find("a")["href"]
        schiaparelli_url_list.append(schiaparelli_urls)
    schiaparelli_url = schiaparelli_url_list[0]
    schiaparelli_title_results = schiaparelli_soup.find_all("h2", class_="title")
    schiaparelli_title_list = []
    for schiaparelli_title_result in schiaparelli_title_results:
        schiaparelli_titles = schiaparelli_title_result.text
        schiaparelli_title_list.append(schiaparelli_titles)
    schiaparelli_title = schiaparelli_title_list[0]
    
    #####################################
    # Scrape Mars Syrtis Hemisphere data
    #####################################
    
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    syrtis_url ="https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(syrtis_url)
    time.sleep(5)
    syrtis_html = browser.html
    syrtis_soup = BeautifulSoup(syrtis_html, "html.parser")
    browser.quit()
    
    ################################################
    # Locate Mars Syrtis Hemisphere image and title
    ################################################

    syrtis_url_results = syrtis_soup.find_all("li")
    syrtis_url_list = []
    for syrtis_url_result in syrtis_url_results:
        syrtis_urls = syrtis_url_result.find("a")["href"]
        syrtis_url_list.append(syrtis_urls)
    syrtis_url = syrtis_url_list[0]
    syrtis_title_results = syrtis_soup.find_all("h2", class_="title")
    syrtis_title_list = []
    for syrtis_title_result in syrtis_title_results:
        syrtis_titles = syrtis_title_result.text
        syrtis_title_list.append(syrtis_titles)
    syrtis_title = syrtis_title_list[0]
    
    #####################################
    # Scrape Mars Valles Hemisphere data
    #####################################
    
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    valles_url ="https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(valles_url)
    time.sleep(5)
    valles_html = browser.html
    valles_soup = BeautifulSoup(valles_html, "html.parser")
    browser.quit()
    
    ################################################
    # Locate Mars Valles Hemisphere image and title
    ################################################

    valles_url_results = valles_soup.find_all("li")
    valles_url_list = []
    for valles_url_result in valles_url_results:
        valles_urls = valles_url_result.find("a")["href"]
        valles_url_list.append(valles_urls)
    valles_url = valles_url_list[0]
    valles_title_results = valles_soup.find_all("h2", class_="title")
    valles_title_list = []
    for valles_title_result in valles_title_results:
        valles_titles = valles_title_result.text
        valles_title_list.append(valles_titles)
    valles_title = valles_title_list[0]
    
    #####################################
    # Create Mars Hemispheres dictionary
    #####################################
    
    hemispheres_data = [
        {"title": cerberus_title, "img_url": cerberus_url},
        {"title": schiaparelli_title, "img_url": schiaparelli_url},
        {"title": syrtis_title, "img_url": syrtis_url},
        {"title": valles_title, "img_url": valles_url},
    ]
    
    ##############################################
    # Create master dictionary and return results
    ##############################################
    
    scrape_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "image_url": image_url,
        "latest_tweet": latest_tweet,
        "html_facts_table": html_facts_table,
        "cerberus_title": hemispheres_data[0]["title"],
        "cerberus_url": hemispheres_data[0]["img_url"],
        "schiaparelli_title": hemispheres_data[1]["title"],
        "schiaparelli_url": hemispheres_data[1]["img_url"],
        "syrtis_title": hemispheres_data[2]["title"],
        "syrtis_url": hemispheres_data[2]["img_url"],
        "valles_title": hemispheres_data[3]["title"],
        "valles_url": hemispheres_data[3]["img_url"]
    }
    
    return scrape_data


        


    
    
    
    
    
    
    

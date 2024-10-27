#!/usr/bin/env python
# coding: utf-8

# In[ ]:
"""basic web scraper using Python libraries like BeautifulSoup."""

pip install requests beautifulsoup4


# In[1]:


import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        return

    # Parse the content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text
    text = soup.get_text(strip=True)
    print("Text content:")
    print(text)

    # Extract links
    links = soup.find_all('a')
    print("\nLinks:")
    for link in links:
        href = link.get('href')
        link_text = link.get_text(strip=True)
        print(f"Text: {link_text}, URL: {href}")

    # Extract images
    images = soup.find_all('img')
    print("\nImages:")
    for img in images:
        img_src = img.get('src')
        img_alt = img.get('alt', 'No alt text')
        print(f"Image Source: {img_src}, Alt Text: {img_alt}")

if __name__ == "__main__":
    url_to_scrape = input("Enter the URL of the website to scrape: ")
    scrape_website(url_to_scrape)
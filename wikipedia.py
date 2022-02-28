# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:35:43 2021

@author: asus
"""

import requests 
import bs4 
import lxml
  
# Taking the query
query = "kota weather"
headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}  

# Generating the url  
url = "https://google.com/search?q=" + query
  
# Sending HTTP request 
request_result = requests.get( url , headers=headers)
  
# Pulling HTTP data from internet 
soup = bs4.BeautifulSoup( request_result.text, "html.parser" )
  
info = soup.find('div', class_='BNeawe').text
    
print(info) 


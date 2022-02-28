# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:35:43 2021

@author: asus
"""

import requests, lxml
from bs4 import BeautifulSoup
headers = {
  "User-agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}
def getInfo(query):
  url = "https://www.google.com/search?q="+query 
  # requests instance
  html = requests.get(url, headers=headers).content
  
  # getting raw data
  soup = BeautifulSoup(html, 'html.parser')    
  # soup = BeautifulSoup(html, 'lxml')
  answer = soup.find_all('div', class_='BNeawe')
  return answer.text
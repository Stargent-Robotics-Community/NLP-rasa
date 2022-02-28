# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:02:05 2021

@author: asus
"""
import requests, lxml
from bs4 import BeautifulSoup

headers = {
  "User-agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
  "q": "32*3/3+12*332-1995",
}

def get_calculator_answerbox():
  html = requests.get('https://www.google.com/search', headers=headers, params=params)
  soup = BeautifulSoup(html.text, 'lxml')

  math_expression = soup.select_one('.XH1CIc')
  calc_answer = soup.select_one('#cwos')

  print(f"Expression: {math_expression}\nAnswer: {calc_answer}")
  return math_expression

answer = get_calculator_answerbox()


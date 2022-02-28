# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:54:15 2021

@author: asus
"""
import requests
import json

def getWeather(city):
    apiKey = "ce40b472ff866867a03fc0af5695600a"
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apiKey

    apiLink = requests.get(url)
    apiData = apiLink.json()

    if apiData['cod'] == 404:   
        print("The city name is invalid ")
    else :
        temp = ((apiData['main']['temp']) - 273.15)
        desc = apiData['weather'][0]['description']
        temp = "{:.2f}".format(temp)
        return ("Its " + str(temp) + " degree Celcius with " + desc + " in " + city)













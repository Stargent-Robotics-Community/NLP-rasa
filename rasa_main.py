# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 00:25:58 2021

@author: asus
"""
import pyttsx3
import requests
import json

import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import os
from pytube import YouTube

from playMusic import play
from weather import getWeather
from wiki import getInfo

sender = "Chintan"
engine = pyttsx3.init()
engine.getProperty("rate")
engine.setProperty("rate", 150)

def speak(input) :
    print(input)
    engine.say(input)
    engine.runAndWait()


bot_msg = ""
while bot_msg != "Bye":
    msg = input("What is your msg \n")
    print("Sending msg now")
    r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={ "sender": sender, "message": msg })
    bot_msg = ''
    for i in r.json():
        bot_msg = i['text']
        
    if bot_msg == '':
        if msg.find('play')==-1 & msg.find('song')==-1:
            if msg.find('weather')==-1 & msg.find('climate')==-1:
                x = getWeather(msg)
                speak("It's, " + x)
            else:
                x = getInfo(msg)
                speak(x)
        else: 
            play(msg)
    else:
        arr = bot_msg.split(' ', 1)
        command = arr[0]
        if(command == 'hi'):
            speak("hello")
        elif(command == 'i'):
            speak("My name is Gyaani, I am a robot made by students of JECRC at Stargent")
        elif(command == 'hru'):
            speak("I am good, full of electrons")
        elif(command == 'jecrc'):
            speak("I will tell you about jecrc")
        elif(command == 'stargent'):
            speak("Stargent is a robotics community at JECRC college. They work mainly on humanoid robots")
        elif(command == 'jok'):
            speak("Hey girl, are you tired, cause your program has been running through my system all night")
        elif(command == 'hp'):
            speak("okay , great") #this is affirmation
        elif(command == 'by'):
            speak("See you soon, bye")
        elif(command == 'wthr'):
            city = arr[1]
            x = getWeather(city)
            speak(x)
        elif(command == 's'):
            song = arr[1]
            play(song)
        elif(command == 'mf'):
            speak("move forward")
        elif(command == 'mb'):
            speak("move backward")
        elif(command == 'mr'):
            speak("move right")
        elif(command == 'ml'):
            speak("move left")
        elif(command=='d'):
            speak("gyaani dance")
        elif(command == 'rm'):
            speak("Recognize me gyaani")
    
            
        
        
        
        
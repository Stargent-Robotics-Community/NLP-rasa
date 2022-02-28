# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 00:25:58 2021

@author: asus
"""
import pyttsx3
import requests

sender = input("What is your name")
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
    print("Sending message now...")
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={ "sender": sender, "message": msg })

    print(end='')
    for i in r.json():
        bot_msg = i['text']
        speak(bot_msg)
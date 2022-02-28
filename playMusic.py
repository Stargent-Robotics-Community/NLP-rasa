# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 12:09:31 2021

@author: asus
"""
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import os
import pafy

from pytube import YouTube

def play(music_name):

    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    inspect = BeautifulSoup(clip.content, "html.parser")
    yt_title = inspect.find_all("meta", property="og:title")

    for concatMusic1 in yt_title:
        pass

    songName = str(concatMusic1['content'])
    print("downloading ... " + songName)
    yt=YouTube(clip2)
    t=yt.streams.filter(only_audio=True)

    t[0].download()
    print("Downloaded ... ")
    songName = songName.replace("|", "")
    songName = songName.replace(".", "")
    songName = songName.replace(":", "")
    songName = songName.replace("'", "")
    songName = songName.replace(",", "")

    import vlc
    p = vlc.MediaPlayer(songName + ".mp4 ")
    p.play()
    
    import keyboard
    while True:
        try :
            if keyboard.is_pressed('p'):
                p.pause() 
                continue
            if keyboard.is_pressed('c'):
                p.play()
                continue 
            if keyboard.is_pressed(' '):
                p.stop() 
                if os.path.exists(songName + ".mp4"):
                    print("Deleting this song file")
                    os.remove(songName + ".mp4")
                    break
                break
        except :
            print("playing song")
            break
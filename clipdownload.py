from datetime import date

import requests
import urllib.request
import os
import json


def clipdownload(link, DIRECTORY):
    invalid = ['/', '\\', ':', '*', '?', '\"', '<', '>', '|']
    payload={}


    headers = {
        'Client-ID': '',
        'Accept': 'application/vnd.twitchtv.v5+json'

    }

    """
    try:
        os.mkdir(DIRECTORY+"\clips\\")
        print("Created \"\\clips\"")
    except:
        print()
    """
    try:
        temp = link["url"].replace("https://clips.twitch.tv", "https://api.twitch.tv/kraken/clips")
        response = (requests.request("GET", temp, headers=headers, data=payload))
        #print(response.json())
        url = response.json()['thumbnails']['small']
        url = url.replace("-preview-260x147.jpg", ".mp4")
        name = link["title"]
    except:
        print("Download unsuccessful\n")
        print("Clip not found: 404")
        return(404)

    invalidtitle = link["title"]
    for x in invalid:
        invalidtitle = invalidtitle.replace(x, "")

    print(("ATTEMPTING TO DOWNLOAD: ") + "{}: ({})\n".format(name,url))
    try:
       urllib.request.urlretrieve(url, (DIRECTORY+"/clips/"+invalidtitle+".mp4"))
       print("Download successful\n")
    except:
       print("Download unsuccessful\n")
    #return (response)

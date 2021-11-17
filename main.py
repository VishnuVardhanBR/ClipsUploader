from fetchcliplink import fetchcliplink
from jsonmanager import jsonread, jsonwrite
import time
import json
import os
from datetime import date
from clipdownload import clipdownload

DIRECTORY = os.getcwd()
invalid = ['/', '\\', ':', '*', '?', '\"', '<', '>', '|']
while True:
    oldlinks = jsonread()
    link = fetchcliplink(oldlinks)
    if link == None:
        print("No clip available right now!")
        break
    jsonwrite(link)
    print(link["title"]+ " "+link["url"])
    clipstatus = clipdownload(link, DIRECTORY)
    if clipstatus == 404:
        continue

    invalidtitle = link["title"]
    for x in invalid:
        invalidtitle = invalidtitle.replace(x, "")
    uploadcommand = "node youtubeupload.js \""+ DIRECTORY +"/clips/"+invalidtitle+".mp4"+"\" \""+ link["title"] + "\" " + "\"Credit: "+link["url"]+"\""
    os.system(uploadcommand)
    deletecommand = "rm \"" + DIRECTORY +"/clips/"+invalidtitle+".mp4"+"\""
    os.system(deletecommand)

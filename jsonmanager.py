import json
import time
import os.path


def jsonread():
    directory = os.getcwd();
    print(directory)
    if os.path.exists(directory+"/oldlinks.json"):
        #print("Path exists")
        with open('oldlinks.json', 'r') as json_file:
            oldlinks = json.load(json_file)
            return oldlinks

    else:
        #print("Path doesn't exist")
        with open('oldlinks.json', 'x+') as f:
            f.write("{\"url\": [], \"time\": [], \"title\": []}")
        oldlinks = {"url": [], "time": [], "title": []}
        return oldlinks


def jsonwrite(link):

    oldlinks = jsonread()
    oldlinks["url"].append(link["url"])
    oldlinks["time"].append(link["time"])
    oldlinks["title"].append(link["title"])



    assert(len(oldlinks["url"]) == len(oldlinks["time"]) == len(oldlinks["title"]))

    timenow = int(time.time())
    i = 0
    while i < len(oldlinks["time"]):
        if (timenow - (oldlinks["time"][i])) >= 172800:
            temp = ["url", "time", "title"]
            for x in temp:
                del oldlinks[x][i]
        else:
            i+=1

    with open("oldlinks.json", "r+") as f:
        content = f.read()
        if len(content) == 0:
            f.write("{\"url\": [], \"time\": [], \"title\": []}")
            print("Created empty dict in json")

    with open('oldlinks.json', 'w') as json_file:
        json.dump(oldlinks, json_file)

from writelink import writelink
import praw

#fetches 1 clip thats above 1000 upvotes; return type = list
def fetchcliplink(links, SUBREDDIT = "LivestreamFail"):
    reddit = praw.Reddit(client_id='VZkMdSXZhyy-ow', client_secret='', user_agent='mainBot')
    subreddit = reddit.subreddit(SUBREDDIT)

    for post in subreddit.top("day"):#, limit = 5):
        postchannel = (str(post.link_flair_text).lower()[9:])
        
        # to take channel name from post via the flair, removing the excess part by checking spaces
        for i in range(0, len(postchannel)):
            #print (i)
            if postchannel[i] == " ":
                postchannel = postchannel[:i]
                break
        #print(postchannel+ " "+ str(post.score)+ "upvotes")

        try:
            if ((post.url).startswith("https://clips.twitch.tv") and post.score >= 1000 and post.url not in links["url"]):
            #print(postchannel)
                dic = {"url": [], "time": [], "title": []}
                dic["url"], dic["time"], dic["title"] = post.url, post.created_utc, post.title                
                return dic
        except:
            return (None)


        
#fetchcliplink()

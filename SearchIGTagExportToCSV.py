from InstagramAPI import InstagramAPI
import datetime
import csv
import os

USERNAME = ""
PASSWORD = ""
TAG = ""


def getTime(text):
    return datetime.datetime.fromtimestamp(int(text)).strftime('%Y-%m-%d %H:%M:%S')


def getTags(tags):
    tagList = list({tag.strip("#") for tag in tags.replace(
        '#', ' #').split() if tag.startswith("#")})
    result = ''
    for i in tagList:
        result += i.encode("utf-8")
        result += ' '

    return result


def getLocation(place):
    location = ''
    if 'location' in place:
        location = place['location']['name']

    return location


api = InstagramAPI(USERNAME, PASSWORD)
api.login()  # login
api.tagFeed(TAG)  # get media list by tag #cat
media_id = api.LastJson  # last response JSON

data = []
for post in media_id["ranked_items"]:
    data.append(post)

results = [[post['caption']['user']['username'].encode("utf-8"),
            getTime(post['caption']['created_at']).encode("utf-8"),
            getTags(post['caption']['text']),
            getLocation(post).encode("utf-8"),
            post['caption']['text'].encode("utf-8")] for post in data]


filename = 'InstagramOutput.csv'
if os.path.exists(filename):
    append_write = 'a'  # append if already exists
else:
    append_write = 'w'  # make a new file if not

with open(filename, append_write) as f:
    writer = csv.writer(f)
    if append_write == 'w':
        writer.writerow(["screen_name", "created_at",
                         "hashtags", "place", "text"])
        writer.writerows(results)
    else:
        writer.writerows(results)

pass
print 'finished!'

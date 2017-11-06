from InstagramAPI import InstagramAPI
import datetime
import csv


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


set(['announcement', 'rocks', 'stackoverflow'])

api = InstagramAPI("", "")
api.login()  # login
api.tagFeed("cat")  # get media list by tag #cat
media_id = api.LastJson  # last response JSON

data = []
for post in media_id["ranked_items"]:
    data.append(post)

results = [[post['caption']['user']['username'].encode("utf-8"),
            getTime(post['caption']['created_at']).encode("utf-8"),
            getTags(post['caption']['text']),
            getLocation(post).encode("utf-8"),
            post['caption']['text'].encode("utf-8")] for post in data]

with open('InstagramOutput.csv', 'r+a') as f:
    writer = csv.writer(f)
    f.seek(0)  # ensure you're at the start of the file..
    first_char = f.read(1)  # get the first character
    if not first_char:
        writer.writerow(["screen_name", "created_at",
                         "hashtags", "place", "text"])
        writer.writerows(results)
    else:
        writer.writerows(results)

pass
print 'finished!'

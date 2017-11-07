from TwitterAPI import TwitterAPI
import csv
import os

consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
SEARCH = ""
COUNT = ""


def getAllHashtags(list):
    hashStr = ''
    for hashes in list:
        hashStr += hashes['text']
        hashStr += ' '

    return hashStr


def getLocation(place):
    location = ''
    if place is not None:
        location += place['full_name'] + ', ' + place['country_code']

    return location


api = TwitterAPI(consumer_key, consumer_secret,
                 access_token_key, access_token_secret)

r = api.request('search/tweets', {'q': SEARCH, 'count': COUNT})

data = []

for item in r:
    data.append(item)

results = [[tweet['user']['screen_name'], tweet['created_at'].replace('+0000 ', ''), getAllHashtags(tweet['entities']['hashtags']),
            getLocation(tweet['place']), tweet['text'].encode("utf-8")] for tweet in data]

filename = 'TwitterOutput.csv'
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

from TwitterAPI import TwitterAPI
import csv

consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""


def getAllHashtags(list):
    hashStr = ''
    for hashes in list:
        hashStr += hashes['text']
        hashStr += ', '

    return hashStr


def getLocation(place):
    location = ''
    if place is not None:
        location += place['full_name'] + ', ' + place['country_code']

    return location


api = TwitterAPI(consumer_key, consumer_secret,
                 access_token_key, access_token_secret)

r = api.request('search/tweets', {'q': '#pizza', 'count': '15'})

data = []

for item in r:
    data.append(item)

results = [[tweet['user']['screen_name'], tweet['created_at'], getAllHashtags(tweet['entities']['hashtags']),
            getLocation(tweet['place']), tweet['text'].encode("utf-8")] for tweet in data]

with open('output.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["screen_name", "created_at", "hashtags", "place", "text"])
    writer.writerows(results)

pass

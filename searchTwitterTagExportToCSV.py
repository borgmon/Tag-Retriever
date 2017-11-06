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
        hashStr += ' '

    return hashStr


def getLocation(place):
    location = ''
    if place is not None:
        location += place['full_name'] + ', ' + place['country_code']

    return location


api = TwitterAPI(consumer_key, consumer_secret,
                 access_token_key, access_token_secret)

r = api.request('search/tweets', {'q': '#cat', 'count': '15'})

data = []

for item in r:
    data.append(item)

results = [[tweet['user']['screen_name'], tweet['created_at'].replace('+0000 ', ''), getAllHashtags(tweet['entities']['hashtags']),
            getLocation(tweet['place']), tweet['text'].encode("utf-8")] for tweet in data]

with open('TwitterOutput.csv', 'r+a') as f:
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

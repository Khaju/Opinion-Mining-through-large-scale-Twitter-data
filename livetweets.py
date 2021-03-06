try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy

ACCESS_TOKEN = 
ACCESS_SECRET = 
CONSUMER_KEY =  
CONSUMER_SECRET = 

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True)
# places = api.geo_search(query="UK", granularity="country")
# place_id = places[0].id
# print('UK id is: ',place_id) #084d0d0155787e9d

searchQuery = "Avengers"
language = "en"
data = []
i=0
# r = api.search(q=searchQuery, count=100, result_type='recent')
# print(r['text'])
for status in tweepy.Cursor(api.search,q = searchQuery, lang=language).items(50):
	jsonObj = status._json
	data.append(jsonObj['text'])
	#info = json.loads(json.loads(jsonObj))

print(len(data))
print(data[0])

with open('Avengers.txt', 'w',  encoding="utf8") as f:
    for item in data:
        f.write("%s\n" % item.replace('\n', ' '))

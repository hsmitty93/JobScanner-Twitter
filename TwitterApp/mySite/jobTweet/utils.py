#Performs a twitter search for new jobs
import tweepy  # x is a string parameter
def search(keyword):
	

	# Load our API credentials

	consumer_key = "XSI1siNxqZeRZYAhnJCyJXUr5"
	consumer_secret = "2601nK0jp0Ku4RBcWtG4kV2GlPBNw2LfuoYjZZoM3gOZF9hIV5"
	access_key = "369689673-Ihgv62x7iTLYoAC3T0KbDu7hVedBzipM4ILTbD1s"
	access_secret = "kptxLj0AZbiRVr0jLyrPlHEoO7UvOiFFRn3B7Psll6ciu"

	# Create twitter API object

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)

	api = tweepy.API(auth)
	# Perfroms a basic search
	# Twitter API docs:
	# https://dev.twitter.com/rest/reference/get/search/tweets

	query = keyword
	tweetList = []
	for tweet in tweepy.Cursor(api.search, q = query, rpp = 100, result_type = "recent", lang = "en").items(100):
		tweetList.append(tweet)
		

	return tweetList





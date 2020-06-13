# Create Twitter developer account and get API key, API secret key, Access toke, Access token secret
auth = tweepy.OAuthHandler(‘API key’, ‘API key secret’)
auth.set_access_token(‘Access Token’, ‘Access token secret')
api = tweepy.API(auth)

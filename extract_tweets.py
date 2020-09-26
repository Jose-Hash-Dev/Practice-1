import pandas as pd
import tweepy
import time
from datetime import datetime

auth = tweepy.OAuthHandler(‘API key’, ‘API key secret’)
auth.set_access_token(‘Access Token’, ‘Access token secret')
api = tweepy.API(auth)


def Extract_Tweets (search_words, date_since, number_of_tweets, number_of_runs):
    # Define a pandas dataframe to store the date:
    db_tweets = pd.DataFrame(
        columns=['username', 'account_description', 'location', 'following', 'followers', 'total_tweets',
                 'user_creation_time',
                 'tweet_creation_time',
                 'retweet_count', 'text', 'hashtags'])

    program_start = time.time()
    for i in range(0, number_of_runs):
        start_run = time.time()

        # Collect tweets using the Cursor object
        # Cursor() returns an object and you can iterate to access the data collected

        tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since, tweet_mode='extended').items(
            number_of_tweets)

        # Store tweets in Python list
        tweets_list = [tweet for tweet in tweets]
        number_of_tweets = 0

    for tweet in tweets_list:
        # Get the values
        username = tweet.user.screen_name  # Username of account
        account_description = tweet.user.description   # Description of account
        location = tweet.user.location   # Location where tweeted
        following = tweet.user.friends_count   # Following list of user
        followers = tweet.user.followers_count   # Number of followers
        total_tweets = tweet.user.statuses_count   # Total tweets
        user_creation_time = tweet.user.created_at   # Tweeter user creation time
        tweet_creation_time = tweet.created_at  # Tweet creation time
        retweet_count = tweet.retweet_count   # Number of Retweets
        hashtags = tweet.entities['hashtags']   # Hashtags in tweet

    try:
        text = tweet.retweeted_status.full_text
    except AttributeError:
        text = tweet.full_text

    # Add the all variables to empty list:
    inf_tweet = [username, account_description, location, following, followers, total_tweets, user_creation_time,
                 tweet_creation_time,
                 retweet_count, text, hashtags]
    # Append to dataframe:
    db_tweets.loc[len(db_tweets)] = inf_tweet
    # Count number of tweets:
    number_of_tweets += 1

    # Run end time:
    end_run = time.time()
    duration_run = round((end_run - start_run) / 60, 2)

    print('number of extracted tweets for run {} : {}'.format(i + 1, number_of_tweets))
    print('time spent {} run to complete is {} minutes'.format(i + 1, duration_run))

    # When all runs completed save all  to csv file:
    # Also add timestamp to files
    to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')

    # Define path and filename:
    path = r'C:\Users\Yusif'
    filename = path + '/data/' + to_csv_timestamp + '_Yusif_Hashimov.csv'
    # Store dataframe in csv with creation date timestamp
    db_tweets.to_csv(filename, index=False)

    program_end = time.time()
    print('Extracting has completed successfully')
    print('Total time to extract is {} minutes.'.format(round(program_end - program_start) / 60, 2))


search_words = "#covid OR #Baku OR #F1 OR #Python #NumPy #Backend OR #DataMining"
date_since = "2019-05-05"
number_of_tweets = 200
number_of_runs = 5

# Call the function Extract_Tweets
Extract_Tweets(search_words, date_since, number_of_tweets, number_of_runs)

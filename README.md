In this article, I will show how to extract data from Twitter step by step. For this purpose, we will use Python Tweepy library.
Prerequisites: Setting up Twitter Developer Account
Before we start, we need Twitter Developer account to use Twitter APIs. To create developer account follow instructions on https://developer.twitter.com/en/apply-for-access. We need 4 information from Twitter developer account: API Key, API secret key, Access token, Access token secret. 
First, let us install libraries. We will use libraries below:

Tweepy

Tweepy is a Python library for accessing the Twitter API. It is great for simple automation and creating twitter bots. You can install Tweepy from PyPI by using pip: 
Pip install tweepy

Pandas

Pandas is used in Python to deal with data analysis and manipulation. To put it in simpler words, Pandas help us to organize data and manipulate the data by putting it in a tabular form.

Time

Python has a module named time to handle time-related tasks. To use functions defined in the module, we need to import the module first.
We start by importing libraries:

import pandas as pd
import tweepy
import time

Then authentication is required to get data from Twitter
auth = tweepy.OAuthHandler(‘API key’, ‘API key secret’)
auth.set_access_token(‘Access Token’, ‘Access token secret')
api = tweepy.API(auth)

# Tweepy Bot
   A Twitter bot is a type of bot software that controls a Twitter account via the Twitter API. The bot software may autonomously perform actions such as tweeting, re-tweeting, liking, following, unfollowing, or direct messaging other accounts. 
     
   The automation of Twitter accounts is governed by a set of automation rules that outline proper and improper uses of automation. Proper usage includes broadcasting helpful information, automatically generating interesting or creative content, and automatically replying to users via direct message. Improper usage includes circumventing API rate limits, violating user privacy, spamming,and sockpuppeting.

How to Make a Twitter Bot: A Full Guide for Beginners

    1. Apply for a developer account
    2. Create a Twitter app
    3. Setup a development environment
    4. Link your Twitter app and dev environment
    5. Program the bot
    6. Test the bot
    
Note : First a full you create the app in twitter developer app https://developer.twitter.com/
       Then after you follow the below instruction.

 *# Installation*

    $ mkdir tweepy-bots
    $ cd tweepy-bots
    $ python3 -m venv venv
    
    $ source ./venv/bin/activate
    $ pip install tweepy
    
# Import
      
    $ import tweepy


# OAuth
      
    import tweepy

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
 
# The API Class
      
    import tweepy

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object

    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    
# Methods for Tweets

    api.update_status("Test tweet from Tweepy Python")
    
# Other API methods on Twitter.Tweepy.Bot.py

    1. Tweets
    2. Retweets
    3. Likes
    4. Direct messages
    5. Favorites
    6. Trends
    7. Media

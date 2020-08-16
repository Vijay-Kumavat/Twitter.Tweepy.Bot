import tweepy
import time
# from decouple import config

# AK : 9j0ZRpfoIFfsrlT7T1ra4s10r 
# AKS : FMjyz6N7ftHxrb2gKBrATGw93QHlhBYEDH2tmOQBa6nAzMUHve
# AT: 1294668148801593344-68sDi6MkTUaNKCwWGAKipk7cQLCHtf
# ATS : E6PEjHGZM6b3KRToZT9FePfMQ2zM92LZh6eTblTlY3kvs

# Authenticate to Twitter
consumer_key = '9j0ZRpfoIFfsrlT7T1ra4s10r'
consumer_secret = 'FMjyz6N7ftHxrb2gKBrATGw93QHlhBYEDH2tmOQBa6nAzMUHve'
key = '1294668148801593344-68sDi6MkTUaNKCwWGAKipk7cQLCHtf'
secret = 'E6PEjHGZM6b3KRToZT9FePfMQ2zM92LZh6eTblTlY3kvs'

# Create API object
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(key,secret)

# wait on rate and limit notify in console
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user=api.me()

# Create a tweet
print("")
print('"Write the a tweet on twitter via bot"')
print("")
api.update_status("Hello Tweepy")

# your timeline
print("")
print('"Your timeline"')
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

# Update the description
print("")
print('"Update the description"')
print("")
api.create_friendship("realpython")
api.update_profile(description="I like Python")

# Favorite tweet and tweet.author
print("")
print('"Favorite tweet and tweet.author"')
print("")
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

# Block user name
print("")
print('"Block user name :"')
print("")
for block in api.blocks():
    print(block.name)

# Followers name and what is he/she tweet via text
print("")
print('"Followers name and what is he/she tweet via text"')
print("")
for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")


# Print user name , decription and location , followers name
print("")
print('"Print user name , decription and location , followers name"')
print("")
user = api.get_user("kvm3coder")

print("User details:")
print("")
print(user.name)
print("")
print(user.description)
print("")
print(user.location)

print("")
print("Last 10 Followers:")
for follower in user.followers():
    print(follower.name)

# Trend results
print("")
print('"Trend results"')
print("")
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])

# Automatic like post from hashtag
hashtag = '#India'
nrTweets=3

print("")
print('"Automatic like post from hashtag"')
print("")
for tweet in tweepy.Cursor(api.search,hashtag).items(nrTweets):
    try:
        print('Tweet Liked 😉')
        tweet.favorite()
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# Automatic like post from username
username = 'kvm3coder'
nrTweets=3

print("")
print('"Automatic like post from username"')
print("")
for tweet in tweepy.Cursor(api.search,username).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# Retweet
hashtag = "#India"
tweetNumber = 5

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            #tweet.like()
            print("Retweet is Done !!!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)
        
searchBot()

# username, followers count, following count and followers username
print("")
print('"Print the username, followers count, following count and followers username"')
print("")
print(user.screen_name)
print("")
print("Followers : ",user.followers_count)
print("Following : ",user.friends_count)
print("")
for follower in user.followers():
    print(follower.name)

print("")
print('"follow the your followers"')


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# follow the your followers
def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            try:
                follower.follow()
                logger.info(f"Following {follower.name}")
            except tweepy.error.TweepError:
                pass

follow_followers(api)

print("")
print('"Unfollowers the any your followers"')

# unfollow the any your followers
def unfollow(api, follower_id = None):
    if not follower_id:
        logger.info("Retrieving current users being followed...")
        for following_id in tweepy.Cursor(api.friends).items():
            try:
                api.destroy_friendship(following_id.id)
                logger.info(f"Unfollowed {following_id.name}")
            except tweepy.error.TweepError:
                pass
    else:
        try:
            api.destroy_friendship(follower_id)
            logger.info(f"Unfollowed {follower_id}...")
        except tweepy.error.TweepError:
            pass

unfollow(api, "@NASA")
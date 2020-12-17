import tweepy
import time
import logging
from twitter_authorise import authorize

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#api authentication
api = authorize("OiA2qCuh8YxkbUeMdIUSc4xuC","93wpHMqxdrMHG46kJG4JnBLN09qCb05hupj3sanBnyJ9CNScjG",
"1226482790750752768-mZWagzWYHm8sxtPtY8D0yFM0E7cUBN","TtMhrxF3fdDjuAs8vOfB28dHqO8pYiSlIMQHMmV77yxFf")

#add usernames of Accounts you want to like the tweets
fav_list = []

def liker():
    '''
    Like all the tweets on user timeline except retweets and mentions
    '''
    like_count = 0
    other_count = 0
    while True:
        others = 0
        for status in api.home_timeline(count = 100):
            favorited = status.favorited
            if not (status.text).startswith("RT") or (status.text).startswith("@") or status.user.screen_name == "sudowick":
                if status.in_reply_to_status_id is None and status.user.screen_name in fav_list :
                    if favorited == True:
                        pass
                    else:
                        try:
                            api.create_favorite(status.id)
                            time.sleep(1)
                            like_count+=1
                        except Exception as e:
                            logger.error("Error on fav", exc_info=True)
                else:
                    others+=1
                    if others%30==0 and favorited == False and status.in_reply_to_status_id is None:
                        try:
                            api.create_favorite(status.id)
                            time.sleep(1)
                            other_count+=1
                        except Exception as e:
                            logger.error("Error on fav", exc_info=True)

        time.sleep(60*6)
        #remaining = int(api.last_response.getheader('x-rate-limit-remaining'))

liker()

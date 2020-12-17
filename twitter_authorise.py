import tweepy
import logging

logger = logging.getLogger()

def authorize(api_key,api_secret,access_token,access_secret):
    '''
    Authenticating
    '''
    auth = tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

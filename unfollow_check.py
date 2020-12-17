import tweepy
import webbrowser
import time
from twitter_authorise import authorize


# Authenticate to Twitter
#Replace below with actual keys from dev account
api = authorize("API key","API Secret","Access Token","Access Secret")


unfollowers_list =[]
lst = []

def unfollowers(name):
    '''
    To check mutuals who unfollowed
    '''
    friendships = api.lookup_friendships(screen_names = name)
    for friendship in friendships:
        if not friendship.is_followed_by:
            unfollowers_list.append(friendship.screen_name)


def check_following():
    '''
    To find usernames of mutuals and send then to unfollowers()
    '''
    following_list=[]
    for page in tweepy.Cursor(api.friends, count=100).pages():
        following_list = [user.screen_name for user in page]
        unfollowers(following_list)

def display():
    '''
    Display the usernames who unfollowed
    '''
    y=1
    for x in unfollowers_list:
        print(y,"  ",x)
        y=y+1

check_following()

display()

def unfollowing():
    while True:
        num = int(input("Enter the number you want to unfollow or Press 0 to exit   "))-1
        if num!= -1:
            lst.append(num)
        else:
            break
    print(lst)
    for user in lst:
        try:
            api.destroy_friendship(unfollowers_list[user])
            print("Unfollowed     ",unfollowers_list[user])
        except (tweepy.RateLimitError, tweepy.TweepError) as e:
                self.error_handling(e)

unfollowing()

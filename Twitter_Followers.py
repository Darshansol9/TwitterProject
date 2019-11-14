"""
This is the script for fetching the followers of  given twitter id and storing it in a file
At one time go, we can fetch upto 300 followers, so sleep has been implemented to wake up after the request is in ready queue.
All the other packages custom created has been imported in this script.
"""

import sys
import auth
import time
import private
import tweepy



class Followers:

    def __init__(self,t_id):
        self.t_id = float('inf')
        
    def twitter_followers(self):
        fp = open('Stream_id.csv','w')
        auth = tweepy.OAuthHandler(private.CONSUMER_KEY,private.CONSUMER_SECRET)
        auth.set_access_token(private.ACCESS_KEY,private.ACCESS_SECRET)
        api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
        ids = []
        page_count = 1
        count = 1
        #18839785 - Modi Used as twitter_id to work on
        
        for user in tweepy.Cursor(api.followers, user_id = self.t_id).items():
            fp.write(user.id_str)
            fp.write("\n")
            count+=1
            if(count%300 == 0):
                print('Sleeping for 900 secs')
                time.sleep(900)
                print('Resumed')
                
        fp.close()
        print("Request Processed")

        
##if __name__=='__main__':
##    tf = Followers(18839785)
##    tf.twitter_followers()  Will be provided from HttpResponse init azure func

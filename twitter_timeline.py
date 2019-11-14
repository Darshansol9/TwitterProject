"""
This script has extracted the tweets of a followers from their timeline and create each followers' file with convention Followers_(No).csv
Error handling is done, where the tweets are unicode and maybe in different languages, so the script translates to non_bmp and encoded the strings to be stored in database.
Req_completed.csv is the list of follower id that has tweeted atleast 200 tweets on it's timeline.
"""


import sys
import tweepy
import auth
import time
import private
import requests
import os


class FetchTweets:

    def __init__(self,twitter_id):
        self.twitter_id = twitter_id
    
    def auth(self):
        auth = tweepy.OAuthHandler(private.CONSUMER_KEY,private.CONSUMER_SECRET)
        auth.set_access_token(private.ACCESS_KEY,private.ACCESS_SECRET)
        api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


    def fetchTweets(self):
        
        self.auth()
        count = 1
        page_count = 1
        follower_count = 1

        followers = open('Req_completed.csv','a+',encoding = 'utf-8')

        for i in open('Followers_List.csv','r'):
            count = 0
            page_count = 1
            string = i.replace('\n',"")
            id_t = int(i)
            print(id_t)
            try:
                
                fp = open('Follower_{}.csv'.format(follower_count),'w',encoding = "utf-8")
                for pages in tweepy.Cursor(api.user_timeline, id = id_t, tweet_mode= "extended",include_rts = False,count=40).pages():
                    for line in pages:
                        fp.write('{twitter_id}|{}|{}|{}|'.format(self.twitter_id,string.replace('\n',""),line.id_str.replace('\n',""),line.full_text.replace('\n',"")))
                        fp.write('\n')
                        count = count+1
                    
                        if(count >= 200):
                            break
                        
                    time.sleep(5)
                    page_count +=1
                    
                    if(count >= 200):
                        fp.close()
                        followers.write(i)
                        followers.write('\n')
                        follower_count +=1
                        print('Breaking when count has reached 200')
                        break
                    
                if(count < 200):
                    fp.close()
                    os.remove('Follower_{}.csv'.format(follower_count))
                    print('Count less than 200, deleted Follower_{}.csv'.format(follower_count))

            except BaseException as e:
                print('Encountered an error ',str(e))
                continue
            
            
        followers.close()        
        print('Request Processed and Completed')


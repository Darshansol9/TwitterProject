
'''
This code import connect_database to connect to database and retreive the fetched result from the created azure sql database
'''
import pyodbc
import sys
import os
import connect_database as cd

class FetchTwitterIds:
    
    def __init__(self,twitter_id):
        self.user_id = str(twitter_id)
        self.string = ''
    
    def fetchIds(self):
        conn = cd.Connect()
        conn.connect_db()
        i = 1
        sql = "Select * from [Twitter].[tweets_info] where follower_id = {}".format("'"+self.user_id+"'")
        row = conn.cursor.execute(sql)
        while row:
            if(i==1):
                i+=1
                row = cursor.fetchone()
                continue
            self.string += str(row).replace("(","").replace(")","")+"\n"
            self.string +="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            row = conn.cursor.fetchone()
        print('Request Processed')

   
##if __name__=='__main__':
##    conn = cd.Connect()
##    conn.connect()
##    cnn = FetchTwitterIds(2418421508) #This is an example for giving twitter_id, but the FetchTwitterIds will get name come from HttpResponse azure function as parameter passing.
##    cnn.fetchIds(conn.cursor)
    





'''
This code uses DSN to connect to database and retreive the fetched result from the created azure sql database
'''

import pyodbc
import sys
import os

class Connect:

    def connect_db(self):
        
        server = 'Database server name'
        database = 'Database name'
        driver= 'SQL Server' #if your database is SQL Server
        username = 'Username'
        password = 'Password'
        #cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        
        #Other way is to create a DSN and fill all the details there so no hard coding in the script.
        dsn = 'Twitter_DSN'
        cnxn = pyodbc.connect('DSN='+dsn+';UID='+username+';PWD='+password)
        self.cursor = cnxn.cursor()
        print('Database connected')

        
    def insert(self):
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)  #Handles the non_bit map characters like emoji's
        path = 'Locations of the tweets files stored'
        os.chdir(path)
        i = 1
        for file in os.listdir('.'):
            for line in open(file,'r',encoding = 'utf-8'):
                try:
                    tokens = line.split('|')
                    twitter_id = tokens[0]
                    follower_id = tokens[1]
                    tweet_id = tokens[2]
                    data = tokens[3].replace("'",'')
                    data = data.translate(non_bmp_map).encode(encoding = "utf-8")
                    i+=1
                    sql = """INSERT INTO [Twitter].[tweets_info] (twitter_id, follower_id, tweet_id,tweets) VALUES ({},{},{},N'{}')""".format(twitter_id,follower_id,tweet_id,data.decode())
                    self.cursor.execute(sql)
                    self.cursor.commit()
                except Exception as e:
                    print(f'Error occured at insert row {i} for file {file} given as {str(e)}')

        print('Request completed')
         
##if __name__=='__main__':
##    cnn = Connect()
##    cnn.connect_db()
##    cnn.insert()


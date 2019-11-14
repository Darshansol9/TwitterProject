import logging
import pyodbc
import azure.functions as func
import connect_database as cd
import Twitter_Followers as tf
import Twitter_Timeline as tt
import private



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    message = req.params.get('body')
    
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        cls1 = tf.Followers(int(name))
        cls1.twitter_followers()         -------> Get the list of 1000 followers and stores in Followers_List.csv file
        
        cls2 = tt.FetchTweets(int(name)) -------> Get the tweets of each follower
        cls2.fetchTweets()

        cls3 = cd.Connect()              ------->   Instaniate object of a class
        cnn.connect_db()                 -------> Connect to db
        cnn.insert()                     -------> Insert into the database
        
        data = 'Twitter_ids for Narendra Modi are as follows\n\n'
        data += '------------------------------\n'
        data += js_w.string
        return func.HttpResponse(data)
    
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )


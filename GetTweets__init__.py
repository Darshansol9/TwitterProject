import logging
import azure.functions as func
import FetchTweetIds as ft

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        cnn = ft.FetchTwitterIds(int(name))
        data = 'The following is the response for the given twitter_id\n\n'
        data += 'Twitter_id\tFollower_id\tTweet_id\tTweets\n\n'
        data += cnn.string
        return func.HttpResponse(data)
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )

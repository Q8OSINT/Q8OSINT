import cherrypy
from TwitterAPI import TwitterAPI
import time, datetime;
import calendar, pytz;
import RobConfig;

@cherrypy.expose
def getTweets(username):
    tweet_list="";
    # check if cherrypy session is initialized otherwise reload token
    if (cherrypy.session['consumer_key'] == ""):
        raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/tokens");
    else:
        api = TwitterAPI(cherrypy.session['consumer_key'], cherrypy.session['consumer_secret'],
                         cherrypy.session['oauth_token'], cherrypy.session['oauth_secret']);

        q = api.request('statuses/user_timeline', {'screen_name': username, 'count': 50});
        tweets = q.json()

        i=0;
        for tweet in tweets:
            hashtags=[]
            for hash in tweet['entities']['hashtags']:
                hashtags.append(hash['text']);

            mentions=[]
            for mention in tweet['entities']['user_mentions']:
                mentions.append(mention['screen_name'])

            RobConfig.tweets.append({
                "timestamp" : tweet['created_at'],
                "user_id" : tweet['user']['id'],
                "user_name" : tweet['user']['name'],
                "text" : tweet['text'],
                "hashtags" : str(hashtags),
                "mentions" : str(mentions)
            });
            i=i+1;
            tweet_list += "<option value=\""+tweet['created_at']+" Sender: "+tweet['user']['name'] +"\">" + "Timestamp: "+tweet['created_at'] + " User: "+ tweet['user']['name'] + "</option>";
    return tweet_list;

